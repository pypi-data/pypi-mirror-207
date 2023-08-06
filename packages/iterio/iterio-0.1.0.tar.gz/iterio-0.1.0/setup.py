# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['iterio']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'iterio',
    'version': '0.1.0',
    'description': 'Python IO using iterators',
    'long_description': '# iterio\nPython IO using iterators\n\n## Installation\n\n```\npip install iterio\n```\n\n## Contributing\n\nSet up the project using [Poetry](https://python-poetry.org/):\n\n```\npoetry install\n```\n\nFormat the code:\n\n```\nmake lint\n```\n\nRun tests:\n\n```\nmake test\n```\n\nCheck for typing and format issues:\n\n```\nmake check\n```\n',
    'author': 'Alexander Malyga',
    'author_email': 'alexander@malyga.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/alexandermalyga/iterio',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
