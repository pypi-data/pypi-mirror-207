# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '..'}

packages = \
['loggers',
 'parser',
 'rob',
 'rob.loggers',
 'rob.parser',
 'rob.ticktick',
 'rob.ticktick.helpers',
 'rob.ticktick.managers',
 'ticktick',
 'ticktick.helpers',
 'ticktick.managers']

package_data = \
{'': ['*'],
 'rob': ['.hypothesis/unicode_data/13.0.0/*',
         '.pytest_cache/*',
         '.pytest_cache/v/cache/*',
         'config/*',
         'data/*',
         'db/*',
         'dist/*']}

install_requires = \
['appdirs>=1.4.4,<2.0.0',
 'deal>=4.23.2,<5.0.0',
 'docopt>=0.6.2,<0.7.0',
 'openai>=0.26.5,<0.27.0',
 'praw>=7.5.0,<8.0.0',
 'pycaw>=20230407,<20230408',
 'pydub==0.25.1',
 'redmail>=0.4.0,<0.5.0',
 'rich>=11.2.0,<12.0.0',
 'rocketry>=2.5.1,<3.0.0',
 'toml>=0.10.2,<0.11.0',
 'typer[all]>=0.7.0,<0.8.0']

setup_kwargs = {
    'name': 'robolson',
    'version': '0.3.81',
    'description': 'My collection of utilty scripts',
    'long_description': None,
    'author': 'Rob L Olson',
    'author_email': 'rob.louis@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1,<3.11',
}


setup(**setup_kwargs)
