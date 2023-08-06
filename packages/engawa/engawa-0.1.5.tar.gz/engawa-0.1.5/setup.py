# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['engawa', 'engawa.misc']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'datasets>=2.8.0,<3.0.0',
 'nltk>=3.8,<4.0',
 'pytorch-lightning>=1.8.6,<2.0.0',
 'sentencepiece>=0.1.97,<0.2.0',
 'sienna>=0.1.5,<0.2.0',
 'tokenizers>=0.13.2,<0.14.0',
 'transformers>=4.25.1,<5.0.0',
 'typer>=0.9.0,<0.10.0',
 'wandb>=0.13.7,<0.14.0']

entry_points = \
{'console_scripts': ['engawa = engawa.cli:app']}

setup_kwargs = {
    'name': 'engawa',
    'version': '0.1.5',
    'description': '',
    'long_description': '# engawa\n\n<img align="center" src="img/logo.jpg" width="200" height="200" />\n\n**NOT YET FULLY TESTED**\n\nA simple implementation to pre-train BART from scratch with your own corpus.\n\n\n# Usage\n\nSoon, I will make this pip-installable with CLI commands but at the moment, you need to run it as a repository.\n\n## Installation\n\n```bash\npip install engawa\n```\n\n## Build tokenizer\n\n```bash\nengawa train-tokenizer --data-path /path/to/train.txt --save-dir /path/to/save\n\n# Checkout other options by\nengawa train-tokenizer --help\n```\n\n## Pre-train BART\n\n```bash\nengawa train-model \\\n  --tokenizer-file /path/to/tokenizer.json \\\n  --train-file /path/to/train.txt \\\n  --val-file /path/to/val.txt \\\n  --default-root-dir /path/to/save/things\n\n# Checkout other options by\nengawa train-model --help\n```\n',
    'author': 'sobamchan',
    'author_email': 'oh.sore.sore.soutarou@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10.8,<4.0.0',
}


setup(**setup_kwargs)
