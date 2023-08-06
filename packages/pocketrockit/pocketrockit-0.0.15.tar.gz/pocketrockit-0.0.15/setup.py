# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pocketrockit']

package_data = \
{'': ['*']}

install_requires = \
['asyncinotify>=4.0.1,<5.0.0',
 'pyfluidsynth>=1.3.1,<2.0.0',
 'pygame>=2.3.0,<3.0.0']

entry_points = \
{'console_scripts': ['pocketrockit = pocketrockit.cli:main',
                     'pri = pocketrockit.cli:main']}

setup_kwargs = {
    'name': 'pocketrockit',
    'version': '0.0.15',
    'description': 'pocketrockit',
    'long_description': '# POCKETROCKIT - A rocket in your pocket that rocks!\n\nOriginal project page: https://projects.om-office.de/frans/pocketrockit.git\n\nWrite a music track in Python and play it while you write it (as you might know it from \n[Sonic Pi](https://sonic-pi.net/), but written in Python (`sonic.py` was not available on PyPi, though)).\n\nWrite melodies, create rythm patterns, define endless simultaneously playing instruments, all in\na .. well .. simple Python syntax.\n\n\n## Installation\n\n```sh\n[<PYTHON> -m] pip[3] install [--upgrade] pocketrockit\n```\n\n## Usage\n\nWorkflow is not quite mature yet, so here is the short version for now.\n\nCreate and enter a separate folder and provide required SoundFont files (configurable later,\nhard-coded for now).\n\nPocketrockt expects two SoundFont files: `instrumental.sf2` and `drums.sf2`. You can download and\nmove/rename any file that works for you, and you can also just create symlinks (this is what I do).\n\nThis is just an example:\n\n```sh\nmkdir mytracks\ncd mytracks\nln -s /usr/share/soundfonts/FluidR3_GM.sf2 instrumental.sf2\nwget https://musical-artifacts.com/artifacts/2744/JV_1080_Drums.sf2\nln -s JV_1080_Drums.sf2 drums.sf2\n```\nThe file `FluidR3_GM.sf2` was shipped with FluidSynth for me, and I got `JV_1080_Drums.sf2` from\n[here](https://musical-artifacts.com/artifacts/2744).\n\n\nCreate a file `myfirsttrack.py` with the following content:\n\n```python\n#!/usr/bin/env python3\n\nfrom pocketrockit import Env, midiseq, player, track\n\n@track\ndef my_first_track(env: Env):\n    """Guess!"""\n\n    env.bpm = 30\n    key = "A5"\n\n    @player\n    def metronome():\n        yield from midiseq("x x x x", channel=128, note=37)\n\n    @player\n    def melody1():\n        yield from midiseq(\n            "| . |"\n            "| .                .                .              (II I)      "\n            "| (II  VI-)        (IV- VI- . II-)  .              (II I)      "\n            "| (II  VI-)        (IV- VI- . II-)  .              (II III)    "\n            "| (IV  . III IV)   (. IV . II)     (III . II III)  (. III . I) "\n            ,\n            key="A5",\n            channel=13,\n            velocity=100,\n        )\n```\n\nNow - keeping the editor open for later use - execute this file. You can either make it executable\nand run it directly or you run `python3` instead:\n\n```sh\nchmod +x myfirsttrack.py\n./myfirsttrack.py\n\n# or\n\npython3 myfirsttrack.py\n```\n\n\n## Development & Contribution\n\n```sh\npip3 install -U poetry pre-commit\ngit clone --recurse-submodules https://projects.om-office.de/frans/pocketrockit.git\ncd pocketrockit\npre-commit install\n# if you need a specific version of Python inside your dev environment\npoetry env use ~/.pyenv/versions/3.10.4/bin/python3\npoetry install\n```\n\n\n## Stuff to read / Sources\n\n### SoundFonts\n\n* https://musescore.org/en/handbook/3/soundfonts-and-sfz-files\n* https://www.producersbuzz.com/category/downloads/download-free-soundfonts-sf2/\n* https://archive.org/details/500-soundfonts-full-gm-sets\n* https://ia802502.us.archive.org/view_archive.php?archive=/27/items/500-soundfonts-full-gm-sets/500_Soundfonts_Full_GM_Sets.zip\n* https://musical-artifacts.com/artifacts?formats=sf2&tags=soundfont\n\n\n### Music stuff\n\n* https://pianoscales.org/major.html\n* https://www.inspiredacoustics.com/en/MIDI_note_numbers_and_center_frequencies\n* https://onlinesequencer.net/181312\n* https://github.com/Rainbow-Dreamer\n* https://github.com/Rainbow-Dreamer/musicpy-daw\n* https://sound.stackexchange.com/\n\n\n### Tech stuff\n\n* https://stackoverflow.com/questions/20023545/running-pyfluidsynth-pyaudio-demo-many-problems-with-alsa-and-jack\n* https://www.ladspa.org/\n\n\n## Notation\n\n* https://mascii.org/\n* https://www.mobilefish.com/tutorials/rtttl/rtttl_quickguide_specification.html\n* https://pypi.org/project/musicpy/\n\n## Troubles\n\n* https://stackoverflow.com/questions/47247814/pygame-midi-init-function-errors\n\n* Missing `/usr/local/share/alsa/alsa.conf`\n```\nALSA lib conf.c:4555:(snd_config_update_r) Cannot access file /usr/local/share/alsa/alsa.conf\nALSA lib seq.c:935:(snd_seq_open_noupdate) Unknown SEQ default\n```\n\n```\nsudo mkdir /usr/local/share/alsa\nsudo ln -s /usr/share/alsa/alsa.conf /usr/local/share/alsa/alsa.conf\n```\n',
    'author': 'Frans Fürst',
    'author_email': 'frans.fuerst+gitlab@protonmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://projects.om-office.de/frans/pocketrockit.git',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
