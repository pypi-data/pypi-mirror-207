# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['detabase']

package_data = \
{'': ['*']}

install_requires = \
['Unidecode>=1.3.6,<2.0.0',
 'anyio>=3.6.2,<4.0.0',
 'deta[async]==1.1.0a2',
 'smartjs>=0.1.0,<0.2.0',
 'starlette>=0.26.1,<0.27.0',
 'type-extensions>=0.1.2,<0.2.0']

setup_kwargs = {
    'name': 'detabase',
    'version': '0.2.6',
    'description': 'Base arquitecture for projects using Deta.',
    'long_description': None,
    'author': 'Daniel Arantes',
    'author_email': 'arantesdv@me.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
