# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['simon_trans_database_models',
 'simon_trans_database_models.alembic',
 'simon_trans_database_models.alembic.versions',
 'simon_trans_database_models.tables']

package_data = \
{'': ['*']}

install_requires = \
['marshmallow==3.14.1', 'sqlalchemy==1.3.18']

setup_kwargs = {
    'name': 'simon-trans-database-models',
    'version': '0.2.0',
    'description': '',
    'long_description': None,
    'author': 'Pintér Tamás',
    'author_email': 'tamas.pinter@pannonszoftver.hu',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
