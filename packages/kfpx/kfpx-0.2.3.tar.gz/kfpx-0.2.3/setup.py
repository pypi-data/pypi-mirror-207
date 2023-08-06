# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kfpx']

package_data = \
{'': ['*']}

install_requires = \
['kfp==1.8.21']

setup_kwargs = {
    'name': 'kfpx',
    'version': '0.2.3',
    'description': 'Extends the kfp package',
    'long_description': 'None',
    'author': 'Hao Xin',
    'author_email': 'haoxinst@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
