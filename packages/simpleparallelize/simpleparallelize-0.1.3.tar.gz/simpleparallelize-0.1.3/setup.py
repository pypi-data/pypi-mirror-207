# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['simpleparallelize']

package_data = \
{'': ['*']}

install_requires = \
['tqdm>=4.65.0,<5.0.0']

setup_kwargs = {
    'name': 'simpleparallelize',
    'version': '0.1.3',
    'description': 'Easy processsing pool setup with a spark-like progress bar',
    'long_description': None,
    'author': 'ericaleman',
    'author_email': 'mail@ericaleman.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
