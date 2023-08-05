# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['more_pathlib']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'more-pathlib',
    'version': '0.2.0',
    'description': "Extending Python's pathlib with more useful functions.",
    'long_description': None,
    'author': 'Timur Kasimov',
    'author_email': 'tkasimov@icloud.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
