# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['madai']

package_data = \
{'': ['*']}

install_requires = \
['nltk>=3.8.1,<4.0.0',
 'pyvi>=0.1.1,<0.2.0',
 'scipy>=1.10.1,<2.0.0',
 'sienna>=0.2.2,<0.3.0',
 'spacy>=3.5.2,<4.0.0',
 'typer==0.7.0']

entry_points = \
{'console_scripts': ['madai = madai.cli:app']}

setup_kwargs = {
    'name': 'madai',
    'version': '0.2.2',
    'description': '',
    'long_description': '# madai\n\nCompute difference between two corpus by using chi2.\nImplementation is based on [Measures for Corpus Similarity and Homogeneity](https://aclanthology.org/W98-1506).\n\nI am not fully sure if this implementation is perfectly follow this paper.\nFeel free to make issues to point out some problems if you find.\n\n## Installation\n\n```\npip install madai\n```\n\n## Usage\n\nmadai implements two ways of computing similarity between two corpus, chi2 and spearman.\nUse spearman when two corpus are different in size.\n\nTwo target corpus need to be text files, each line containing one document/sentence.\n\n```\nmadai chi2 /path/to/corpus/a /path/to/corpus/b\n\n# or\n\nmadai spearman /path/to/corpus/a /path/to/corpus/b\n```\n\nTo view parameters, run,\n```\nmadai --help\n```\n',
    'author': 'sobamchan',
    'author_email': 'oh.sore.sore.soutarou@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<3.12',
}


setup(**setup_kwargs)
