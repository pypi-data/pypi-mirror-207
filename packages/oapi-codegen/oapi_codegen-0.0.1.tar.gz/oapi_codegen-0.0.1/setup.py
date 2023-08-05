# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['generator']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['openapi-codegenerator = generator.main:app']}

setup_kwargs = {
    'name': 'oapi-codegen',
    'version': '0.0.1',
    'description': '',
    'long_description': '',
    'author': 'Thiago Leal',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ThiagoLeal11/oapi-codegen',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.7.0,<4.0.0',
}


setup(**setup_kwargs)
