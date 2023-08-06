# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['testing_juhwanlee123']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'testing-juhwanlee123',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'juhwanlee-diquest',
    'author_email': 'juhwanlee@diquest.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<3.9',
}


setup(**setup_kwargs)
