# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['square']

package_data = \
{'': ['*']}

install_requires = \
['backoff',
 'colorama',
 'colorlog',
 'google',
 'google-api-python-client',
 'jsonpatch',
 'pydantic>=1.8',
 'pyyaml',
 'requests']

entry_points = \
{'console_scripts': ['square = square.main:main']}

setup_kwargs = {
    'name': 'kubernetes-square',
    'version': '1.3.2',
    'description': '',
    'long_description': None,
    'author': 'Oliver Nagy',
    'author_email': 'olitheolix@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10',
}


setup(**setup_kwargs)
