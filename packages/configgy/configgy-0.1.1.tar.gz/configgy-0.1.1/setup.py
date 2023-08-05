# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['configgy']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0', 'configparser>=5.3.0,<6.0.0', 'toml>=0.10.2,<0.11.0']

setup_kwargs = {
    'name': 'configgy',
    'version': '0.1.1',
    'description': 'A subtle config loader for python',
    'long_description': '# Configgy\n\nA subtle Python package for loading configuration files without having to specify the file type.\n\n## Installation\n\nYou can install the package from PyPI using pip:\n\n```bash\npip install configgy\n```\n\n## Usage\n\nHere\'s an example of how to use the package to load a configuration file:\n\n```python\nfrom configgy.loader import ConfigLoader\n\ndata = ConfigLoader().load_config_file("file.json")\n```\n\nThe `load_config` function takes a single argument, the path to the configuration file. It will automatically detect the file type and use the appropriate loader.\n\nCurrently, the package supports the following file types:\n\n- INI\n- YAML\n- TOML\n- JSON\n',
    'author': 'baniasbaabe',
    'author_email': 'banias@hotmail.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/baniasbaabe/configgy',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
