# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['reamber',
 'reamber.algorithms',
 'reamber.algorithms.analysis',
 'reamber.algorithms.convert',
 'reamber.algorithms.generate',
 'reamber.algorithms.osu',
 'reamber.algorithms.pattern',
 'reamber.algorithms.pattern.combos',
 'reamber.algorithms.pattern.filters',
 'reamber.algorithms.playField',
 'reamber.algorithms.playField.parts',
 'reamber.algorithms.timing',
 'reamber.algorithms.timing.utils',
 'reamber.algorithms.utils',
 'reamber.base',
 'reamber.base.lists',
 'reamber.base.lists.notes',
 'reamber.bms',
 'reamber.bms.lists',
 'reamber.bms.lists.notes',
 'reamber.o2jam',
 'reamber.o2jam.lists',
 'reamber.o2jam.lists.notes',
 'reamber.osu',
 'reamber.osu.lists',
 'reamber.osu.lists.notes',
 'reamber.quaver',
 'reamber.quaver.lists',
 'reamber.quaver.lists.notes',
 'reamber.sm',
 'reamber.sm.lists',
 'reamber.sm.lists.notes']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=9.5.0,<10.0.0',
 'PyYAML>=6.0,<7.0',
 'Unidecode>=1.3.6,<2.0.0',
 'matplotlib>=3.7.1,<4.0.0',
 'numpy>=1.24.3,<2.0.0',
 'osrparse>=6.0.2,<7.0.0',
 'pandas>=2.0.1,<3.0.0',
 'tqdm>=4.65.0,<5.0.0']

setup_kwargs = {
    'name': 'reamber',
    'version': '0.1.8',
    'description': 'Vertical Scrolling Rhythm Game Toolset',
    'long_description': "![license](https://img.shields.io/github/license/Eve-ning/reamberPy)\n![dls](https://img.shields.io/pypi/dm/reamber)\n![codecov-coverage](https://img.shields.io/codecov/c/github/Eve-ning/reamberPy)\n![codefactor](https://img.shields.io/codefactor/grade/github/Eve-ning/reamberPy)\n![version](https://img.shields.io/pypi/v/reamber)\n\n# Reamber (Py) \n\n[:blue_book: Wiki](https://eve-ning.github.io/reamberPy/index.html) & [Getting Started](https://eve-ning.github.io/reamberPy/info/GettingStarted.html)\n\n`pip install reamber`\n\n------\n\nVSRG Toolbox for data extraction, manipulation & analysis.\n\n# Features\n\n- Game Support: osu!mania, StepMania, BMS and partially O2Jam files.\n- Algorithms: Map IO, Conversion, Map Image Generation, Pattern Extraction\n- Data Architecture: Pandas DataFrame Integration\n\n> This is built on pandas `DataFrame`, thus, if you need more control, you can \nretrieve the underlying `DataFrame` via the `.df` property on many reamber classes. \n\n# Status\n\nThis is in alpha, names and references will change without notice.\nWe highly recommended to fix version in requirements.\n\n## For Developers, By Developers\n\nA growing amount of osu!mania players are interested in programming.\nThe best way to learn is to relate it to something that you're familiar with.\n\nThat's why I'm making a library that allows you to tamper with your favorite\ngames, and learn on the way.\n\n# Migrating to >v0.1.1 Releases\n\nMigrating to `>0.1.1` means spending time updating **a lot** of names.\n\nMajor changes in `0.1.1` include many differences in naming. \nOnly update it if you don't plan mind spending time refactoring.\n",
    'author': 'Evening',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
