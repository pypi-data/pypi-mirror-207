# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['opsml']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'opsml',
    'version': '0.1.0',
    'description': '',
    'long_description': '# Coming Soon',
    'author': 'Thorrester',
    'author_email': '48217609+thorrester@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
