# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['flask_constance', 'flask_constance.admin', 'flask_constance.backends']

package_data = \
{'': ['*'], 'flask_constance.admin': ['templates/*']}

install_requires = \
['Flask-Admin[admin]>=1.6.1,<2.0.0',
 'Flask-SQLAlchemy[fsqla]>=2.5.1,<3.0.0',
 'Flask-WTF[admin]>=1.1.1,<2.0.0',
 'Flask>=2.0.1,<3.0.0',
 'SQLAlchemy[fsqla]>1.4,<2.0',
 'blinker[signals]>=1.6,<2.0']

setup_kwargs = {
    'name': 'flask-constance',
    'version': '0.1.0',
    'description': 'Dynamic settings for Flask applications',
    'long_description': 'None',
    'author': 'Ivan Fedorov',
    'author_email': 'inbox@titaniumhocker.ru',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/TitaniumHocker/Flask-Constance',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
