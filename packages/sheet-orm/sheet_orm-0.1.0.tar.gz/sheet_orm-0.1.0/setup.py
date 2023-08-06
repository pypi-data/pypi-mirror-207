# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sheet_orm']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'sheet-orm',
    'version': '0.1.0',
    'description': '',
    'long_description': '# sheet-orm\n\n---\n\n<p align="center">\n<a href="https://github.com/SheetOrg/sheet-orm/actions?query=workflow%3ATests+event%3Apush+branch%3Amain" target="_blank">\n    <img src="https://github.com/SheetOrg/sheet-orm/actions/workflows/test.yaml/badge.svg?branch=main&event=push" alt="Test">\n</a>\n<a href="https://codecov.io/gh/SheetOrg/sheet-orm" target="_blank">\n    <img src="https://img.shields.io/codecov/c/github/SheetOrg/sheet-orm?color=%2334D058" alt="Coverage">\n</a>\n<a href="https://pypi.org/project/sheet-orm/" target="_blank">\n    <img alt="PyPI" src="https://img.shields.io/pypi/v/sheet-orm?color=%2334D058&label=pypi%20package" alt="Package version">\n</a>\n<a href="https://pypi.org/project/sheet-orm/" target="_blank">\n    <img src="https://img.shields.io/pypi/pyversions/sheet-orm?color=%2334D058" alt="Supported Python versions">\n</a>\n</p>\n\n## Installation\n\n```bash\npip install sheet-orm\n```\n',
    'author': 'Stanislav Zmiev',
    'author_email': 'szmiev2000@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ovsyanka83/sheet-orm',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10',
}


setup(**setup_kwargs)
