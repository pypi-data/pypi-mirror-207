# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['goatl']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'goatl',
    'version': '0.6.3',
    'description': 'The goat logger',
    'long_description': '<div align="center">\n<img src="assets/images/goatlbanner.png" alt="goatl logo"/>\n\n</div>\n\n---\n\n# goatl\n\n<div align="center">\n\n[![Build status](https://github.com/EytanDn/goatl/workflows/build/badge.svg?branch=master&event=push)](https://github.com/EytanDn/goatl/actions?query=workflow%3Abuild)\n[![Python Version](https://img.shields.io/pypi/pyversions/goatl.svg)](https://pypi.org/project/goatl/)\n[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/EytanDn/goatl/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)\n\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n![Coverage Report](assets/images/coverage.svg)\n\n</div>\n\n## Installation\n\n```bash\npip install -U goatl\n```\n\nor install with `Poetry`\n\n```bash\npoetry add goatl\n```\n\n## Purpose\n\ngoatl provides a simple and easy to use logging interface for python projects.\nby replacing repetitive boilerplate code with a simple function call:\nthe magic "log" function.\n\n```python\nfrom goatl import log\n```\n\ngoatl usage is all about the log\n\n## Usage\n\n### as a function\n\n```python\nlog("hello world")\n# 2020-07-19 16:00:00,000 - goatl - INFO - hello world\nlog.debug("hello world?")\n# 2020-07-19 16:00:00,000 - goatl - DEBUG - hello world?\nlog.info("do you know the answer of {} + {}?", 41, 1)\n# 2020-07-19 16:00:00,000 - goatl - INFO - do you know the answer of 41 + 1?\n```\n\n### as a method decorator\n\n```python\n@log\ndef foo(x, y):\n    return x + y\n\n@log.debug\ndef bar():\n    return "hello world"\n\n@log.debug(return_level=log.info)\ndef baz(x):\n    return x*2\n\nfoo(1, 2)\n# ... INFO - foo called with args: (1, 2), kwargs: {}\n# ... DEBUG - foo returned: 3\nbar()\n# ... DEBUG - bar called with args: (), kwargs: {}\n# ... DEBUG - bar returned: hello world\nbaz(3)\n# ... DEBUG - baz called with args: (3,), kwargs: {}\n# ... INFO - baz returned: 6\n```\n\n### as a class decorator\n\n```python\n@log\nclass Foo:\n    def __init__(self, x):\n        self.x = x\n\n    def bar(self, y):\n        return self.x + y\n\n    @log.warn\n    def baz(self):\n        return self.x * 2\n\n\nfoo = Foo(1)\n# ... INFO - Instantiated Foo with args: (1,), kwargs: {}\nfoo.bar(2)\n# ... INFO - Foo.bar called with args: (2,), kwargs: {}\n# ... DEBUG - Foo.bar returned: 3\nfoo.baz()\n# ... WARNING - Foo.baz called with args: (), kwargs: {}\n# ... WARNING - Foo.baz returned: 2\n```\n\n### configurations shortcuts\n\n```python\nfile_formatter = log.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")\nlog.addFileHandler("foo.log", fmt=file_formatter)\nlog.addStreamHandler(fmt="%(levelname)s - %(message)s")\nlog.basicConfig(...)\n```\n\n### logging interface #not implemented yet\n\nI do plan to implement goatl\'s interaction with logging through an interface\nsuch that it will be possible to use goatl with any logging backend.\n\n```python\nlog.setBackend(logging)\nlog.setBackend(loguru)\nlogger = log.getLogger("foo")\n```\n\n## core concepts\n\nIn order to justify the existence of goatl,\nit must fulfill three important core concepts:\n\n1. Unobtrusive - it should not interfere\\* with the existing code.\n2. Ease of use - using it should be intuitive and pythonic.\n3. Clean - the amount of code added to the existing code should be minimal.\n\n<sub>\\* - logging will always carry a performative cost, goatl will aim at keeping it to a minimum.</sub>\n\n### means\n\nextensive testing of goatl must be implemented to ensure that it does not interfere with the existing code.\nit should be tested by wrapping other popular libraries and modules with goatl.\nthis will ensure that goatl does not interfere with the existing code.\nperformance tests should be implemented to measure the performance cost of goatl,\nit should not exceed a reasonable threshold, in comparison to adding logging manually.\n\n### main features\n\nthe log function provides an easy interace for:\n\n- out of and in context log calls\n- wrapping existing functions with log calls\n- wrapping existing classes with log calls\n- wrapping existing modules with log calls #not implemented yet, is this even possible?\n- logging configuration #not implemented yet\n- support multiple logging backends #not implemented yet\n\nall in an intuitive and pythonic way.\n\n## Releases\n\nYou can see the list of available releases on the [GitHub Releases](https://github.com/EytanDn/goatl/releases) page.\n\n## License\n\n[![License](https://img.shields.io/github/license/Eytandn/goatl)](https://github.com/EytanDn/goatl/blob/master/LICENSE)\n\nThis project is licensed under the terms of the `MIT` license. See [LICENSE](https://github.com/eytandn/goatl/blob/master/LICENSE) for more details.\n\n## Citation\n\n```bibtex\n@misc{goatl,\n  author = {goatl},\n  title = {goat logger},\n  year = {2023},\n  publisher = {GitHub},\n  journal = {GitHub repository},\n  howpublished = {\\url{https://github.com/EytanDn/goatl}}\n}\n```\n',
    'author': 'goatl',
    'author_email': 'EytanDn@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/EytanDn/goatl',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
