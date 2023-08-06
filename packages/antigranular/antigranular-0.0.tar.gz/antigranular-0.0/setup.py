# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['antigranular']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'antigranular',
    'version': '0.0',
    'description': 'Placeholder [Antigranular](https://antigranular.com) client package to access competitions and datasets with private python execution.',
    'long_description': '# AntigranularClient\nPlaceholder [Antigranular](https://antigranular.com) client package to access competitions and datasets with private python execution.\n\nAntigranular is a community-driven, open-source platform that merges confidential computing and differential privacy. This creates a secure environment for handling unseen data with confidence.\n\n##### Note: This package is just a placeholder and contains no functionaliyy as of now. Visit [antigranular.com](https://antigranular.com) for more inforation about the product.',
    'author': 'Oblivious Software',
    'author_email': 'support@oblivious.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
