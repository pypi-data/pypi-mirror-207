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
    'version': '0.5.1',
    'description': "Wrapper for Google's Python API.",
    'long_description': '# googleapiutils2\n\nUtilities for\n[Google\'s v2 Python API](https://github.com/googleapis/google-api-python-client).\nCurrently supports sections of the following resources:\n\n-   Drive: `FilesResource`, `...`\n-   Sheets: `SpreadsheetsResource`, `...`\n-   Geocoding\n\n## Quickstart\n\nThis project requires Python `^3.10` to run.\n\nSeveral dependencies are needed, namely the aforesaid Google Python API, but also\nGoogle\'s oauth library, and `requests`. Pre-bundled for ease of use are the fairly\nmonolithic `google-api-stubs`, which greatly improves the usage experience.\n\n### via [`poetry`](https://python-poetry.org/docs/)\n\nInstall poetry, then run\n\n> poetry install\n\nAnd you\'re done.\n\n## Drive\n\n...\n\n## Sheets\n\nSimple example:\n\n```python\n...\ncreds = get_oauth2_creds(client_config=config_path)\nsheets = Sheets(creds=creds)\n\nsheet_id = "id"\nSheet1 = SheetsValueRange(sheets, sheet_id, sheet_name="Sheet1")\n\nrows = [\n    {\n        "Heyy": "99",\n    }\n]\nSheet1[2:3, ...].update(rows)\n```\n\nWhat the above does is: - Get the OAuth2 credentials from the `client_config.json`\nfile - create a `Sheets` object thereupon. - Create a `SheetsValueRange` object, which\nis a wrapper around the `spreadsheets.values` API. - Update the range `Sheet1!A2:B3`\nwith the given rows.\n\nNote the slicing syntax, which will feel quite familiar for any Python programmer.\n\n### SheetSlice\n\nA `SheetsValueRange` object can be sliced in a similar manner to that of a Numpy array.\nThe syntax is as follows:\n\n    slc = Sheet[rows, cols]\n\nWherein `rows` and `cols` are either integers, slices of integers (stride is not\nsupported), strings (in A1 notation), or ellipses (`...`).\n\n```py\nix = SheetSlice["Sheet1", 1:3, 2:4] #  "Sheet1!B2:D4"\nix = SheetSlice["Sheet1", "A1:B2"]  #  "Sheet1!A1:B2"\nix = SheetSlice[1:3, 2:4]           #  "Sheet1!B2:D4"\nix = SheetSlice["A1:B2"]            #  "Sheet1!A1:B2"\nix = SheetSlice[..., 1:3]           #  "Sheet1!A1:Z3"\n```\n\n`SheetSlice` object can also be used as a key into a `SheetsValueRange` object, or a\ndictionary (to use in updating a sheet\'s range, for example). Further, a\n`SheetsValueRange` object can be sliced in a similar manner to that of a `SheetSlice`\nobject, and also be used as a dictionary key.\n',
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
