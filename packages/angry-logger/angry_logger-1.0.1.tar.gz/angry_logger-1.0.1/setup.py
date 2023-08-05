# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['angry_logger']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'angry-logger',
    'version': '1.0.1',
    'description': 'Make your logging more passive agressive. Or just agressive agressive.',
    'long_description': '\n[![version](https://img.shields.io/pypi/v/angry-logger)](https://pypi.org/project/angry-logger/)\n[![licence](https://img.shields.io/pypi/l/angry-logger)](https://github.com/GitToby/angry-logger)\n\n# Angry Logging Made Easy\n\nDo you want to show your logger to be more passive aggressive? maybe just actual aggressive? This is the library for\nyou.\n\n## Installation\nYou can install via pip!\n```shell\npip install angry-logger\n```\n\n## Usage\nWhen deciding your project needs more aggression, all you have to do is tell the Angry Logger to go to town. Like so.\n```python\nimport angry_logger\nangry_logger.start()\n```\nIf you\'re not a fan of naughty words, you can tell the angry logger to be less of a potty mouth.\n```python\nimport angry_logger\nangry_logger.start(potty_mouth=False)\n```\n\nFrom here, use your logging as you normally would.\n```python\nimport angry_logger\nimport logging\n\nangry_logger.start(potty_mouth=False)\nlogging.basicConfig(level=logging.DEBUG)\n\ntest_logger = logging.getLogger("test_logger")\n\ntest_logger.debug("this is a test debug message")\ntest_logger.info("this is a test info message")\ntest_logger.warning("this is a test warning message")\ntest_logger.error("this is a test error message")\n```\n\nThis will output your new normal, information hidden behind abuse.\n```\nDEBUG:test_logger:Can I go home now? this is a test debug message\nINFO:test_logger:this is a test info message. But what do you mean by that?\nWARNING:test_logger:Did you do something stupid? Look: this is a test warning message\nERROR:test_logger:this is a test error message????? Are you *****ING kidding me??\n```',
    'author': 'Toby Devlin',
    'author_email': 'toby@tobydevlin.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/GitToby/angry-logger',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
