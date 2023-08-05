# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aiofauna']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp-devtools>=1.0.post0,<2.0',
 'aiohttp-sse>=2.1.0,<3.0.0',
 'aiohttp>=3.8.4,<4.0.0',
 'aiohttp_cors>=0.7.0,<0.8.0',
 'iso8601>=1.1.0,<2.0.0',
 'pydantic[dotenv]>=1.10.7,<2.0.0']

entry_points = \
{'console_scripts': ['dev = aiofauna.cli:dev']}

setup_kwargs = {
    'name': 'aiofauna',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'Oscar Bahamonde',
    'author_email': 'oscar.bahamonde.dev@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
