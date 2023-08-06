# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['simpleparallelize']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'simpleparallelize',
    'version': '0.1.0',
    'description': 'A package that makes it easy to parallelize for loops',
    'long_description': None,
    'author': 'ericaleman',
    'author_email': 'mail@ericaleman.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
