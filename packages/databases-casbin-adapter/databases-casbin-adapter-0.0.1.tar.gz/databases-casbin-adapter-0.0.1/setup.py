# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['casbin_databases_adapter']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy==1.4.46', 'asynccasbin==1.1.8', 'databases==0.7.0']

setup_kwargs = {
    'name': 'databases-casbin-adapter',
    'version': '0.0.1',
    'description': 'An adapter for PyCasbin that implemented by Databases library which support async process',
    'long_description': '# Databases Casbin Adapter\n\nThis is an Adapter for [PyCasbin](https://github.com/casbin/pycasbin) that implemented using [Databases](https://www.encode.io/databases) connection to achieve async process\n\n## Commands\n\n* `make check` to run mypy\n* `make test` to run unit test that written using pytest\n',
    'author': 'isasetiawan',
    'author_email': '10252610+isasetiawan@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
