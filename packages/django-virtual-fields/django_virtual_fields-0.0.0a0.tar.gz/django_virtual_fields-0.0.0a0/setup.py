# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['virtual_fields']

package_data = \
{'': ['*']}

install_requires = \
['Django>=3.2.0', 'typing-extensions>=4.4.0', 'zana>=0.2.0a4,<0.3.0']

setup_kwargs = {
    'name': 'django-virtual-fields',
    'version': '0.0.0a0',
    'description': 'Virtual `django` fields.',
    'long_description': 'None',
    'author': 'David Kyalo',
    'author_email': 'davidmkyalo@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
