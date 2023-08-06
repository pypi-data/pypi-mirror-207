# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nlcomputer', 'nlcomputer.core']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'nlcomputer',
    'version': '0.0.1',
    'description': 'Natural Language Computer (see https://github.com/fixie-ai/nlc)',
    'long_description': 'None',
    'author': 'Fixie.ai Team',
    'author_email': 'hello@fixie.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
