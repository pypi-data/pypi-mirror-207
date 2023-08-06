# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['elasticityproject']

package_data = \
{'': ['*']}

install_requires = \
['mayavi>=4.8.1,<5.0.0', 'numpy>=1.24.3,<2.0.0', 'vtk>=9.2.6,<10.0.0']

setup_kwargs = {
    'name': 'elasticityproject',
    'version': '0.1.1.1',
    'description': 'A collection of classes and routines to help the treatment and presentation of single and polycrystal elastic properties',
    'long_description': None,
    'author': 'EEL-USP-Elasticity Group',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
