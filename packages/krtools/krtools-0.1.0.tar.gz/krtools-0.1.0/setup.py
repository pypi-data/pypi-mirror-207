# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['krtools', 'krtools.sqltools']

package_data = \
{'': ['*']}

install_requires = \
['csvreader>=0.0.4,<0.0.5',
 'psycopg2>=2.9.6,<3.0.0',
 'pydantic[all]>=1.10.7,<2.0.0',
 'python-dotenv>=1.0.0,<2.0.0',
 'sqlalchemy>=2.0.9,<3.0.0',
 'typer[all]>=0.9.0,<0.10.0']

entry_points = \
{'console_scripts': ['krtools = krtools.__main__:app']}

setup_kwargs = {
    'name': 'krtools',
    'version': '0.1.0',
    'description': '',
    'long_description': '# KR Tools\n\nA personal toolkit for data malnipulation. A WIP.\n\n## Installation\n\nPackage is not yet available on PyPI, so use `git clone` on this repository.\n\nThen use `poetry install` to install all project dependencies.\n\nFinally, use `poetry run krtools --help` for usage instructions.\n\n## Usage\n\nSee documentation in `docs/`. Use `$ sphinx-build docs/ docs/_build` to build\nAPI reference.',
    'author': 'Kevin Riley',
    'author_email': 'kp.riley@icloud.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
