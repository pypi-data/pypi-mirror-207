# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['peal']

package_data = \
{'': ['*']}

install_requires = \
['datasets>=2.12.0,<3.0.0',
 'evaluate>=0.4.0,<0.5.0',
 'peft>=0.3.0,<0.4.0',
 'seqeval>=1.2.2,<2.0.0',
 'streamlit>=1.22.0,<2.0.0',
 'torch>=2.0.0,<3.0.0',
 'transformers>=4.28.1,<5.0.0']

setup_kwargs = {
    'name': 'peal',
    'version': '0.1.0',
    'description': 'A package dedicated to using PEFT for active-learning, hence PEAL.',
    'long_description': '# lazy-learner\nA package dedicated to using PEFT for active-learning.\n',
    'author': 'david',
    'author_email': 'david.m.berenstein@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
