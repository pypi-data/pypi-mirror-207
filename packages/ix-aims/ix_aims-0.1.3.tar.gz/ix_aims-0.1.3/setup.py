# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ix_aims', 'ix_aims.imgs']

package_data = \
{'': ['*']}

install_requires = \
['PyAutoGUI>=0.9.53,<0.10.0',
 'arrow>=1.2.3,<2.0.0',
 'hakai-api>=1.4.0,<2.0.0',
 'opencv-python>=4.7.0.72,<5.0.0.0',
 'pillow>=9.5.0,<10.0.0',
 'rich>=13.3.5,<14.0.0',
 'typer>=0.9.0,<0.10.0']

entry_points = \
{'console_scripts': ['autoix = ix_aims.cli:main']}

setup_kwargs = {
    'name': 'ix-aims',
    'version': '0.1.3',
    'description': 'iX Capture automation with AIMS data',
    'long_description': '# auto-ix-capture\n',
    'author': 'Taylor Denouden',
    'author_email': 'taylor.denouden@hakai.org',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
