# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sample_git_diffs']

package_data = \
{'': ['*']}

install_requires = \
['pandas']

entry_points = \
{'console_scripts': ['diff2markdown = sample_git_diffs.to_md:cli',
                     'sample-git-diffs = '
                     'sample_git_diffs.sample_git_diffs:cli']}

setup_kwargs = {
    'name': 'sample-git-diffs',
    'version': '0.3.1',
    'description': '',
    'long_description': '# sample-git-diffs\n\n```\nSample git diffs uniformly wrt. number of changes per file. The output is formatted as a .diff file.\n\noptional arguments:\n  -h, --help            show this help message and exit\n  --n N                 Total number of diffs to be sampled\n  --diffstat DIFFSTAT   Custom git diff command for the sampling probabilities\n  --diffcommand DIFFCOMMAND\n                        Custom git diff command for the actual diff\n```\n\nFor example, if you want to draw a sample of 25 diffs from the folder data/, you run\n\n```\nsample-git-diffs --diffstat "git diff --stat data/" --n 25\n```\n\nTo save this to changes.diff, you run\n\n```\nsample-git-diffs --diffstat "git diff --stat data/" --n 25 > changes.diff\n```\n\nThere\'s also a script that converts the generated .diff / .patch files into markdown.\n\n```\nusage: diff2markdown [-h] --path PATH [--username USERNAME] [--reponame REPONAME] [--branch BRANCH]\n\noptional arguments:\n  -h, --help           show this help message and exit\n  --path PATH\n  --username USERNAME\n  --reponame REPONAME\n  --branch BRANCH\n```\n\nFor example, if you want to convert the changes.diff file into markdown, assuming that the repo is called \'sample-git-diffs\', you\'re on branch \'main\' and the github username is \'testuser\', you run\n\n```\ndiff2markdown --path changes.diff --username testuser --reponame sample-git-diffs --branch main\n```',
    'author': 'ninpnin',
    'author_email': 'you@example.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ninpnin/sample-git-diffs',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
