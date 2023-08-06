# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['ib110hw_testing', 'ib110hw_testing.testing', 'ib110hw_testing.transformation']

package_data = \
{'': ['*']}

install_requires = \
['exrex', 'hypothesis', 'ib110hw']

setup_kwargs = {
    'name': 'ib110hw-testing',
    'version': '0.1.9',
    'description': 'Package used for testing homework assignments in the IB110 course at FI MUNI.',
    'long_description': None,
    'author': 'Martin Pilát',
    'author_email': '8pilatmartin8@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.8,<4.0.0',
}


setup(**setup_kwargs)
