# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ditti_boost']

package_data = \
{'': ['*']}

install_requires = \
['farcaster>=0.7.7,<0.8.0']

entry_points = \
{'console_scripts': ['ditti-boost = ditti_boost.cli:main']}

setup_kwargs = {
    'name': 'ditti-boost',
    'version': '1.0.1',
    'description': '',
    'long_description': "# Ditti Boost\n\nDitti Boost is a command-line tool that automates following and unfollowing users on Farcaster. It provides a simple way to grow your network, find new users, and manage your connections on the platform.\n\n## Features\n\n- Follow users based on different criteria:\n  - Copy a user's following\n  - Follow new users\n  - Follow collection owners\n- Unfollow users based on different criteria:\n  - Unfollow all users\n  - Unfollow non-follow back users\n  - Unfollow collection owners\n  - Unfollow users with no casts\n  - Unfollow no casts within x days\n\n## Installation\n\n_This project requires python3.10_\n\nTo install Ditti Boost, run the following command:\n\n```\npip install ditti-boost\n\nditti-boost\n```\n\n## Usage\n\nTo use Ditti Boost, first navigate to the project directory and run the following command:\n\n```\npoetry env use 3.10\npoetry install\npoetry run python ditti_boost/cli.py\n```\n\nYou will be prompted to enter either an access token or a mnemonic phrase. Then, you can choose from various follow and unfollow options.\n\n## Contributing\n\nContributions are welcome! If you'd like to help improve Ditti Boost, please feel free to open an issue, submit a pull request, or suggest new features.\n\n## License\n\nDitti Boost is licensed under the MIT License.\n",
    'author': 'alex paden',
    'author_email': 'padenalex0@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
