# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['qctrlreleasenoter']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0,<9.0',
 'gitpython>=3.1.31,<4.0.0',
 'packaging>=23.0,<24.0',
 'pyinflect>=0.5.1,<0.6.0']

entry_points = \
{'console_scripts': ['release_noter = qctrlreleasenoter.cli:main']}

setup_kwargs = {
    'name': 'qctrl-release-noter',
    'version': '0.9.0',
    'description': 'Q-CTRL Release Noter',
    'long_description': '# Q-CTRL Release Noter\n\nThe Q-CTRL Release Noter Python package provides a command line tool that generates the\nrecommended release notes for a GitHub package from Q-CTRL.\n\n## Installation\n\nInstall the Q-CTRL Release Noter with:\n\n```shell\npip install qctrl-release-noter\n```\n\n## Usage\n\nIn the repository whose release notes you want to generate, run:\n\n```shell\nrelease_noter\n```\n\nYou can also specify the path of the repository:\n\n```shell\nrelease_noter /path/to/repository\n```\n\nTo prefill the information on the GitHub release page, use:\n\n```shell\nrelease_noter --github\n```\n',
    'author': 'Q-CTRL',
    'author_email': 'support@q-ctrl.com',
    'maintainer': 'Q-CTRL',
    'maintainer_email': 'support@q-ctrl.com',
    'url': 'https://q-ctrl.com',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.12',
}


setup(**setup_kwargs)
