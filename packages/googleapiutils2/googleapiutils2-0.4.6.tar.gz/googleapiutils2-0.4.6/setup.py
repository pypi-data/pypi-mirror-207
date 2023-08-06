# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['googleapiutils2',
 'googleapiutils2.drive',
 'googleapiutils2.geocode',
 'googleapiutils2.sheets']

package_data = \
{'': ['*']}

install_requires = \
['cachetools>=5.2.1,<6.0.0',
 'google-api-python-client-stubs>=1.11.0,<2.0.0',
 'google-api-python-client>=2.47.0,<3.0.0',
 'google-auth-httplib2>=0.1.0,<0.2.0',
 'google-auth-oauthlib>=0.5.1,<0.6.0',
 'pandas>=1.5.3,<2.0.0',
 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'googleapiutils2',
    'version': '0.4.6',
    'description': "Simple and convenient wrapper for Google's Python API.",
    'long_description': 'None',
    'author': 'Mike Babb',
    'author_email': 'mike7400@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
