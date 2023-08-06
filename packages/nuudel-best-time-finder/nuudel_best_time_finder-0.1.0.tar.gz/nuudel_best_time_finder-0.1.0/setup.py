# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nuudel_best_time_finder']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=2.0.1,<3.0.0', 'requests>=2.30.0,<3.0.0']

setup_kwargs = {
    'name': 'nuudel-best-time-finder',
    'version': '0.1.0',
    'description': '',
    'long_description': '# Nuudel best time finder\n\nIn a poll like this:\n\n|         | 2023-06-05 | 2023-06-07 | 2023-06-08 | 2023-06-12 | ... |\n|---------|------------|------------|------------|------------|-----|\n| Alice   | Yes        | No         | No         | Yes        | ... |\n| Bob     | No         | No         | No         | Yes        | ... |\n| Carl    | Yes        | Yes        | No         | No         | ... |\n| Dave    | Yes        | No         | No         | Yes        | ... |\n| Eve     | No         | No         | No         | Yes        | ... |\n| Francis | No         | No         | No         | No         | ... |\n| ...     | ...        | ...        | ...        | ...        | ... |\n\na common task is to find the set of two or more days that cover as many people as\npossible.\n\nThis tool works with the poll service nuudel (<https://nuudel.digitalcourage.de/>),\nreads the data directly from a given poll and finds the best combinations for any number\nof times.\n\n## Install\n\nInstall using pip:\n\n```console\npip install nuudel-best-time-finder\n\n```\n\n## How to use\n\nSay we have a nuudel poll at: <https://nuudel.digitalcourage.de/nuudel-poll-id> and want\nto find two dates that cover the most amount of people simply run:\n\n```python\nfrom nuudel_best_time_finder import find_best_times\n\nfind_best_times(poll = "{nuudel-poll-id}", n =2, results_file = "results.csv")\n```\n\nThe results are then written to a file called `results.csv` with three columns:\n\n* Time combinations\n* Number of people covered by the combination\n* Percent coverage out of all participants\n',
    'author': 'Philip Hackstock',
    'author_email': '20710924+phackstock@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
