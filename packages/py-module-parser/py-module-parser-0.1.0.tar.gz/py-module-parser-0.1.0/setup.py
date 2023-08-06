# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['py_module_parser']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'py-module-parser',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Iuliia Volkova',
    'author_email': 'xnuinside@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
