# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['oz_defender', 'oz_defender.relay']

package_data = \
{'': ['*']}

install_requires = \
['pycognito>=2022.12.0,<2023.0.0',
 'pytest-mock>=3.10.0,<4.0.0',
 'requests>=2.28.2,<3.0.0']

entry_points = \
{'console_scripts': ['test = scripts:test']}

setup_kwargs = {
    'name': 'oz-defender',
    'version': '0.1.1',
    'description': '',
    'long_description': "# oz-defender\nPackage for interacting with Open Zeppelin's Defender API\n\n## Installation\nUsing `pip`\n```bash\n$ pip install oz-defender\n```\n\nUsing `poetry`\n```bash\n$ poetry add oz-defender\n```\n\n## Usage\nThis package is intended to mirror as closely as possible the [defender-client](https://github.com/OpenZeppelin/defender-client) JavaScript package to provide a unified API across languages.\n\n### Relay\nSee [defender-relay-client](https://www.npmjs.com/package/defender-relay-client) for this module's inspiration.\n\nFor the [Relay API](https://docs.openzeppelin.com/defender/relay-api-reference#relay-client-module), used for administrating your team's relayers:\n```python\nfrom oz_defender.relay import RelayClient\n\nrelay = RelayClient(api_key='defender-team-api-key', api_secret='defender-team-api-secret')\nrelay.list_relayers()\n```\n\nFor the [Relayer API](https://docs.openzeppelin.com/defender/relay-api-reference#relay-signer-module), used for transaction related operations with a specific relayer\n```python\nfrom oz_defender.relay import RelayerClient\n\nrelayer = RelayerClient(api_key='relayer-api-key', api_secret='relayer-api-secret')\nrelayer.list_transactions()\n```\n\n## Contributing\n`oz-defender` is under active development so we welcome any and all contributions to improve the package!\n### Issues\nTo make it as simple as possible for us to help you, please include the following when [creating an issue](https://github.com/franklin-systems/oz-defender/issues):\n- OS\n- python version\n- `oz-defender` version\n\n**NOTE: Unless the change you're making is minor, please open an issue in GitHub to discuss a change before opening a PR**\n\n### Development\nThis package is developed using [poetry](https://python-poetry.org/docs/). Make sure its installed on your machine and peep the documentation to familiarize yourself with its commands.\n\n1. Clone this repository\n```bash\n$ git clone https://github.com/franklin-systems/oz-defender\n```\n2. Install `pre-commit` and its hooks\n```bash\n$ pip install pre-commit\n```\nor if you're using macOS\n```bash\n$ brew install pre-commit\n```\nthen\n```bash\n$ pre-commit install\n```\n3. Check out a new branch\n```bash\n$ git checkout my-new-feature-branch\n```\n4. Commit and create your PR with a detailed description and tag the GitHub issue that your work addresses\n\n### Testing `oz_defender` locally\n1. Install (if it's your first time) or update deps\n```bash\n$ poetry install\n```\nor\n```bash\n$ poetry update\n```\n2. Initialize a shell in `poetry` virtual env\n```bash\n$ poetry shell\n```\n3. Enter a python REPL\n```bash\n(oz-defender-py3.10) $ python3\n```\n4. Import `oz_defender` and off you go\n```python\n>>> from oz_defender import *\n>>> relayer = RelayerClient(api_key='relayer-api-key', api_secret='relayer-api-secret')\n```\n5. Quit the python REPL and re-initialize to pick up code changes as you develop\n",
    'author': 'Franklin Developers',
    'author_email': 'developers@hellofranklin.co',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/franklin-systems/oz-defender',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
