# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['butterflymx', 'butterflymx.graphql', 'butterflymx.models']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.4,<4.0.0',
 'beautifulsoup4>=4.12.2,<5.0.0',
 'ruff>=0.0.265,<0.0.266']

setup_kwargs = {
    'name': 'butterflymx',
    'version': '0.1.1',
    'description': 'A reverse-engineered ButterflyMX app API wrapper',
    'long_description': '# ButterflyMX\nA reverse-engineered ButterflyMX app API wrapper\n',
    'author': 'Milo Weinberg',
    'author_email': 'iapetus011@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Iapetus-11/ButterflyMX',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
