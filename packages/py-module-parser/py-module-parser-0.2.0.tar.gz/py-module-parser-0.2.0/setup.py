# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['py_module_parser']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'py-module-parser',
    'version': '0.2.0',
    'description': 'Python Module Parser is a library that parses Python modules and outputs information about imports, functions, variables, and their corresponding line numbers. This makes it easier to analyze and understand the structure of your Python code.',
    'long_description': '# Python Module Parser\n![badge1](https://img.shields.io/pypi/v/py-module-parser) ![badge2](https://img.shields.io/pypi/l/py-module-parser) ![badge3](https://img.shields.io/pypi/pyversions/py-module-parser)![workflow](https://github.com/xnuinside/py-module-parser/actions/workflows/main.yml/badge.svg)\n\nPython Module Parser is a library that parses Python modules and outputs information about imports, functions, variables, and their corresponding line numbers. This makes it easier to analyze and understand the structure of your Python code.\n\nTo get more samples of output - check tests: tests/test_py_module_parser.py\n\nThis project inspired by https://github.com/xnuinside/codegraph and https://github.com/xnuinside/py-models-parser and will be used as a parser inside them in the future. \n\n## Features\n\n- Parse Python modules and extract information about imports, functions, and variables\n- Identify line numbers for each import, function, and variable\n- Represent the extracted information in a structured format\n\n## Installation\n\nTo install the Python Module Parser library, use `pip`:\n\n```bash\n    pip install py-module-parser\n```\n\n\n## Usage\nHere\'s a simple example of how to use the Python Module Parser library:\n\n```python\nfrom py_module_parser import PyModulesParser\n\nsource_code = """from django.db import models\n\n\nclass Musician(models.Model):\n    first_name = models.CharField(max_length=50)\n    last_name = models.CharField(max_length=50)\n    instrument = models.CharField(max_length=100)\n\n"""\nparsed_output = PyModulesParser(source_code).parse()\nprint(parsed_output)\n```\n\nThis will output:\n\n```python\n[\n    FromImportOutput(\n        lineno_start=1,\n        lineno_end=1,\n        module=\'django.db\',\n        imports=[\n            ImportOutput(\n                lineno_start=1,\n                lineno_end=1,\n                name=\'models\',\n                alias=None,\n                node_type=\'import\'\n            )\n        ],\n        node_type=\'from_import\'\n    ),\n    ClassOutput(\n        lineno_start=4,\n        lineno_end=7,\n        name=\'Musician\',\n        parents=[\'models.Model\'],\n        attrs=[\n            VariableOutput(\n                lineno_start=5,\n                lineno_end=5,\n                name=\'first_name\',\n                type_annotation=None,\n                default=FuncCallOutput(\n                    lineno_start=5,\n                    lineno_end=5,\n                    func_name=\'models.CharField\',\n                    args=[],\n                    kwargs={\'max_length\': 50},\n                    node_type=\'func_call\'\n                ),\n                properties={},\n                node_type=\'variable\'\n            ),\n            VariableOutput(\n                lineno_start=6,\n                lineno_end=6,\n                name=\'last_name\',\n                type_annotation=None,\n                default=FuncCallOutput(\n                    lineno_start=6,\n                    lineno_end=6,\n                    func_name=\'models.CharField\',\n                    args=[],\n                    kwargs={\'max_length\': 50},\n                    node_type=\'func_call\'\n                ),\n                properties={},\n                node_type=\'variable\'\n            ),\n            VariableOutput(\n                lineno_start=7,\n                lineno_end=7,\n                name=\'instrument\',\n                type_annotation=None,\n                default=FuncCallOutput(\n                    lineno_start=7,\n                    lineno_end=7,\n                    func_name=\'models.CharField\',\n                    args=[],\n                    kwargs={\'max_length\': 100},\n                    node_type=\'func_call\'\n                ),\n                properties={},\n                node_type=\'variable\'\n            )\n        ],\n        node_type=\'class\'\n    )\n]\n```\n\nTo parse from file, you can use method `parse_from_file`\n\n```python\nfrom py_module_parser import parse_from_file\n\nparsed_output = parse_from_file(file_path=\'path_to/python_module.py\')\nprint(parsed_output)\n```\n',
    'author': 'Iuliia Volkova',
    'author_email': 'xnuinside@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/xnuinside/py-module-parser',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
