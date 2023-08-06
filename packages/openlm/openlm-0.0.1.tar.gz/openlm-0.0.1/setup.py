# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['openlm']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'openlm',
    'version': '0.0.1',
    'description': 'Drop-in OpenAI-compatible that can call LLMs from other providers',
    'long_description': '# OpenLM Python Library\n\nDrop-in OpenAI-compatible that can call LLMs from other providers.',
    'author': 'Matt Rickard',
    'author_email': 'pip@matt-rickard.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
