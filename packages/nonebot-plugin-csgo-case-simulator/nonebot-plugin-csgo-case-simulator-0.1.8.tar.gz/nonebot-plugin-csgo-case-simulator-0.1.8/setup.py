# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot-plugin-csgo-case-simulator']

package_data = \
{'': ['*'], 'nonebot-plugin-csgo-case-simulator': ['font/*', 'json/*']}

install_requires = \
['Pillow>=9.5.0,<10.0.0',
 'httpx>=0.24.0,<0.25.0',
 'nonebot-adapter-onebot>=2.2.3,<3.0.0',
 'nonebot2>=2.0.0-rc.4,<3.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-csgo-case-simulator',
    'version': '0.1.8',
    'description': 'a nonebot based csgo case simulator',
    'long_description': None,
    'author': 'Roy',
    'author_email': 'lyt2980999208@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
