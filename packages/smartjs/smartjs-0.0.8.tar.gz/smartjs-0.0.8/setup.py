# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['smartjs']

package_data = \
{'': ['*']}

install_requires = \
['Unidecode>=1.3.6,<2.0.0']

setup_kwargs = {
    'name': 'smartjs',
    'version': '0.0.8',
    'description': '',
    'long_description': None,
    'author': 'Daniel Victor',
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
