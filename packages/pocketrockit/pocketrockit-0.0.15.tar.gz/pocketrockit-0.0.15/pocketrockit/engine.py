#!/usr/bin/env python3

"""POCKETROCKIT engine
"""

import asyncio
import concurrent
import logging
import threading
import time
from asyncio import sleep as async_sleep
from collections.abc import (
    Generator,
    Iterable,
    Iterator,
    MutableMapping,
    MutableSequence,
    Sequence,
)
from contextlib import ExitStack
from dataclasses import dataclass, field
from importlib.machinery import SourceFileLoader
from importlib.util import module_from_spec, spec_from_file_location
from itertools import chain, count
from pathlib import Path
from types import ModuleType

from asyncinotify import Inotify, Mask

from .commons import Event
from .midi_io import midi_input_device, midi_output_device
from .misc import Singleton, colored, error, keyboard_reader, setup_logging, watchdog

MidiCmd = tuple[int, int, None | int]
CmdTrace = tuple[int, int, int]
Command = tuple[CmdTrace, str, Sequence[MidiCmd]]
Player = Generator[Command, None | int, None]

STEP_SIZE = 4 * 4 * 3
EMPTY_COMMAND: Command = (-1, -1, -1), "", []


@dataclass
class Env:
    """Some global environment"""

    bpm: int = 60


@dataclass
class Stage(metaclass=Singleton):
    """Access to the currently played music"""

    env: Env = field(default_factory=Env)
    active: bool = False
    # On startup we want the current track definition to be free from errors. Verified will
    # be set once we successfully read from all generators
    verified: bool = False
    players: Iterable[tuple[str, Player]] = field(default_factory=list)
    new_track: None | MutableSequence[tuple[str, Player]] = None
    file_to_track: str = ""
    tick: int = -1
    pause: bool = False
    step: bool = False


def load_module(filepath: str | Path) -> ModuleType:
    """(Re)loads a python module specified by @filepath"""
    print(f"load module '{Path(filepath).stem}'")
    spec = spec_from_file_location(Path(filepath).stem, filepath)
    if not (spec and spec.loader):
        raise RuntimeError("Could not load")
    module = module_from_spec(spec)
    assert module
    assert isinstance(spec.loader, SourceFileLoader)
    loader: SourceFileLoader = spec.loader
    # here the actual track definition takes place
    loader.exec_module(module)
    return module


def note_generator() -> Iterator[Iterable[MidiCmd]]:
    """Brings all players together and cleans up played notes"""
    active_notes: MutableMapping[tuple[int, int], int] = {}
    stage = Stage()

    for tick in count():
        stage.tick = tick

        if tick % STEP_SIZE == 0:
            print(f"== {tick // 16} {tick // 4} {tick % 4} {tick} ==")

        all_commands: MutableSequence[MidiCmd] = []
        for name, stream in stage.players:
            try:
                source_pos, origin, commands = next(stream)
                if commands:
                    print(f"{name}: {source_pos}:{origin} => {commands}")
                if commands:
                    all_commands.extend(commands)
            except StopIteration:
                pass
            except Exception as exc:  # pylint: disable=broad-except
                if not stage.verified:
                    raise
                error(f"exception in play: {exc}")

        stoppers = []
        for (active_channel, active_note), store_tick in list(active_notes.items()):
            # send noteoff for any still played note
            if tick - store_tick > 12:
                stoppers.append((active_channel, active_note, None))
                del active_notes[active_channel, active_note]
        for channel, note, _velocity in all_commands or []:
            # print((channel, note), active)
            if (channel, note) in active_notes:
                # send noteoff for next note to be played
                stoppers.append((channel, note, None))
                del active_notes[channel, note]

            active_notes[channel, note] = tick

        # print(tick, active_notes)
        yield chain(stoppers, all_commands)


@watchdog
async def music_loop() -> None:
    """Main loop collecting instructions to send it to MIDI"""
    with midi_output_device("fluidsynth") as midi_out:
        while True:
            # wait for players to emerge (otherwise `tick` won't start at 0)
            if Stage().players:
                break
            print("no players yet..")
            await async_sleep(0.2)
            continue

        last_now = time.time()

        for notes in note_generator():
            for channel, note, velocity in notes:
                if velocity is None:
                    # print("OF", (channel, note))
                    midi_out.noteoff(channel, note)
                else:
                    Stage().step = False
                    # print("ON", (channel, note, velocity))
                    midi_out.noteon(channel, note, velocity)

            while True:
                # make me absolute please
                waitfor = 60 / Stage().env.bpm / STEP_SIZE
                await async_sleep(max(0, (waitfor - (time.time() - last_now))))
                last_now = time.time()
                if not Stage().pause or Stage().step:
                    break


@watchdog
async def watch_changes() -> None:
    """Watches for file changes in track definition file and reload on change"""
    stage = Stage()
    load_module(stage.file_to_track)
    with Inotify() as inotify:
        inotify.add_watch(
            Path(Stage().file_to_track).parent,
            Mask.CLOSE_WRITE,
        )
        async for event in inotify:
            print(event.path, event.mask)
            try:
                assert event.path
                load_module(event.path)
            except Exception as exc:  # pylint: disable=broad-except
                error(f"Caught {exc}")


def logger() -> logging.Logger:
    """Named logger"""
    return logging.getLogger("pr.engine")


@watchdog
async def handle_events(event_queue: asyncio.Queue[Event], terminator: threading.Event) -> None:
    """Main event handler"""
    logger().debug(">> handle_events")
    try:
        while not terminator.is_set():
            try:
                event = await event_queue.get()
                if event.type in {pygame.WINDOWCLOSE, pygame.QUIT}:
                    logger().debug("quit/windowclose")
                    break
                if event.type == pygame.MOUSEMOTION:
                    pass
                elif event.type == pygame.TEXTINPUT:
                    pass
                elif event.type == pygame.KEYDOWN:
                    pass
                elif event.type == pygame.KEYUP:
                    pass
                elif event.type == "note_on":
                    print("NOTEON", event)
                elif event.type == "note_off":
                    print("NOTEOFF", event)
                else:
                    logger().debug("event %s", event)
            except Exception as exc:  # pylint: disable=broad-except
                print(exc)
        logger().debug("handle_events: got termination signal")

    finally:
        logger().debug("<< handle_events")
        terminate(terminator)


def terminate(terminator: threading.Event) -> None:
    """Sends a signal to async tasks to tell them to stop"""
    try:
        terminator.set()
        time.sleep(0.2)
        asyncio.get_event_loop().stop()
        # pygame.event.post(pygame.event.Event(pygame.MOUSEMOTION))
        time.sleep(0.2)
    except Exception as exc:  # pylint: disable=broad-except
        logger().error("terminator got: %r", exc)


@watchdog
async def handle_keyboard(loop: asyncio.BaseEventLoop, terminator: threading.Event) -> None:
    """Handles key press event"""
    try:
        async for key in keyboard_reader(loop, terminator):
            if key == " ":
                logger().info(colored("SPACE", "yellow"))
                Stage().pause = not Stage().pause
            elif key == ".":
                logger().info(colored("STEP", "yellow"))
                Stage().pause = True
                Stage().step = True
            elif key == "q":
                logger().info(colored("QUIT", "yellow"))
                break
            else:
                logger().info(colored(key, "yellow"))
        logger().info("Keyboard loop stopped - terminate program")
        terminate(terminator)
    except RuntimeError as exc:
        logger().warning("Could not run keyboard handler: %s", exc)


def run() -> None:
    """Runs the pocketrockit event loop forever"""
    setup_logging()

    event_queue: asyncio.Queue[Event] = asyncio.Queue()
    terminator = threading.Event()
    loop = asyncio.get_event_loop()

    with ExitStack() as block:
        pool = block.enter_context(concurrent.futures.ThreadPoolExecutor())

        loop.run_in_executor(
            pool,
            midi_input_device,
            "pygame",
            ["OP-1", "Sylphyo", "USB MIDI Interface", "Midi Through"],
            event_queue,
            terminator,
        )
        asyncio.ensure_future(handle_keyboard(loop, terminator))
        # asyncio.ensure_future(handle_events(event_queue, terminator))
        asyncio.ensure_future(music_loop())
        asyncio.ensure_future(watch_changes())

        try:
            loop.run_forever()
        except KeyboardInterrupt:
            logger().debug("KeyboardInterrput in main()")
        finally:
            terminate(terminator)
            logger().debug("finally - loop.run_forever()")
