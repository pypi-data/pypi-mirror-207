# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['acrosort_tex']

package_data = \
{'': ['*']}

install_requires = \
['rich>=13.3.5,<14.0.0']

entry_points = \
{'console_scripts': ['acrosort = acrosort_tex.sorter:main']}

setup_kwargs = {
    'name': 'acrosort-tex',
    'version': '0.1.1',
    'description': '',
    'long_description': "# acrosort-tex\n\n`acrosort-tex` is a Python Command Line App to sort your acronyms in your `.tex` by their shortform.\n\n## Installation\n\nYou can install acrosort-tex using pip (note the underscore):\n\n```bash\npip install acrosort_tex\n```\n\n## Usage\n\nTo use `acrosort-tex`, you first need to create a `.tex` file with a list of acronyms (see in `examples` for an example file).\n\nIt doesn't matter if there are other TeX commands before or after the `acronym` block.\n\nTo sort the acronyms, run the following command:\n\n```bash\nacrosort <input_file.tex> <output_file.tex>\n```\n\nFor example:\n\n```bash\nacrosort examples/List_Of_Abbreviations.tex acronyms.tex\n```\n\nThis will create a new `.tex` file called `sorted_acronyms.tex` with the sorted acronyms, while everything else isn't touched.\n\nIt will also find the longest key to set the width of the shortform column in the acronym block.\n\n## License\n\n`acrosort_tex` is licensed under the MIT License. See the LICENSE file for more information.\n",
    'author': 'baniasbaabe',
    'author_email': 'banias@hotmail.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/baniasbaabe/acrosort-tex/tree/main',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
