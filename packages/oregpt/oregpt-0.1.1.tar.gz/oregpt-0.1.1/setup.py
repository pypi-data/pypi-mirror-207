# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['oregpt']

package_data = \
{'': ['*']}

install_requires = \
['openai>=0.27.6,<0.28.0', 'prompt-toolkit>=3.0.38,<4.0.0', 'pyyaml>=6.0,<7.0']

entry_points = \
{'console_scripts': ['oregpt = oregpt.main:main']}

setup_kwargs = {
    'name': 'oregpt',
    'version': '0.1.1',
    'description': 'A tiny GPT CLI tool',
    'long_description': '# oregpt\n![workflow](https://github.com/shinichi-takayanagi/oregpt/actions/workflows/main.yml/badge.svg)\n[![license](https://img.shields.io/github/license/shinichi-takayanagi/oregpt.svg)](https://github.com/shinichi-takayanagi/oregpt/blob/master/LICENSE)\n[![release](https://img.shields.io/github/release/shinichi-takayanagi/oregpt.svg)](https://github.com/shinichi-takayanagi/oregpt/releases/latest)\n[![python-version](https://img.shields.io/pypi/pyversions/oregpt.svg)](https://pypi.org/project/oregpt/)\n[![pypi](https://img.shields.io/pypi/v/oregpt?color=%2334D058&label=pypi%20package)](https://pypi.org/project/oregpt)\n\nA tiny GPT CLI tool.\nYou can chat with the GPT model developped by OpenAI and save the conversation as json.\n\n![oregpt](https://user-images.githubusercontent.com/24406372/236609166-0f2385b1-fd9e-4810-b80d-c19c44d13411.gif)\n\n## Installation\n### Get your own OpenAI API Key\nAssuming you have an environment variable with key named `OPENAI_API_KEY`.\nIf you don\'t have a OpenAI API key [visit here](https://platform.openai.com/account/api-keys), generate one and add it as an environment variable\n\n```bash\nexport OPENAI_API_KEY=<YOUR-OPENAI-API-KEY>\n\n```\n\n### Instal from PyPI\nYou can install the package using pip:\n\n```bash\n$ pip install oregpt\n```\n\n## Usage\nOnce you have installed oregpt, you can run it by typing:\n```bash\n$ oregpt\n```\n\n## Configuration\nYou can specify the place of conversation `log`,\n[style (color etc)](https://python-prompt-toolkit.readthedocs.io/en/master/pages/advanced_topics/styling.html)\nand\n[the model supported in /v1/chat/completions endpoint provided by OpenAI](https://platform.openai.com/docs/models/overview)\nin `~/.oregpt/config.yml`\n```yaml\n❯ cat ~/.oregpt/config.yml\nlog: /tmp/oregpt/\nopenai:\n    model: gpt-3.5-turbo\n# You can also specify OpenAI\'s API key here\n#     api_key: <your-api-key>\ncharacter:\n    user:\n        name: Me\n        style: "#00BEFE"\n    assistant:\n        name: AI\n        style: "#87CEEB"\n    system:\n        name: System\n        style: "#cc0000"\n```\n',
    'author': 'Shinichi Takayanagi',
    'author_email': 'shinichi.takayanagi@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/shinichi-takayanagi/oregpt',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
