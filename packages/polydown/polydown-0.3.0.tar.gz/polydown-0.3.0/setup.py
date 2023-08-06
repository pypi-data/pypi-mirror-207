# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['polydown']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.3,<4.0.0', 'requests>=2.30.0,<3.0.0', 'rich>=13.3.0,<14.0.0']

entry_points = \
{'console_scripts': ['polydown = polydown.__main__:cli']}

setup_kwargs = {
    'name': 'polydown',
    'version': '0.3.0',
    'description': 'Batch downloader for polyhaven (polyhaven.com)',
    'long_description': '![screenshot](https://user-images.githubusercontent.com/16024979/134770914-bbc829ac-f1aa-43eb-adf4-9d189379d307.gif)\n<div align="center">\n<a href="https://github.com/agmmnn/polydown">\n<img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/agmmnn/polydown"></a>\n<a href="https://pypi.org/project/polydown/">\n<img alt="PyPI" src="https://img.shields.io/pypi/v/polydown"></a>\n\nBatch downloader for [polyhaven.com](https://polyhaven.com/). Download hdris, textures and models in any sizes you want. This project uses Poly Haven\'s [Public API](https://github.com/Poly-Haven/Public-API).\n</div>\n\n# Installation\n\n- `pip install polydown`\n\n# How to Use\n```\n$ polydown hdris\n\n# download all available sizes of all hdris into current folder.\n> 🔗(polyhaven.com/hdris[\'all sizes\'])=>🏠\n```\n```\n$ polydown <asset_type>\n\n# download all assets of this asset type to the current folder in all available sizes.\n# asset types: "hdris", "textures", "models".\n```\n```\n$ polydown textures -c\n\n# list of category in the given asset type.\n```\n```\n$ polydown hdris -f hdris_down -s 2k 4k\n\n# download all hdris with given sizes into "hdris_down" folder.\n# /if there is no such folder it will create it./\n> 🔗(polyhaven.com/hdris[\'2k\', \'4k\'])=>🏠(hdris_down)\n```\n## Example Usage\n\n```\n$ polydown models -c decorative -f folder -s 1k\n\n# download all "models" with "1k textures" in the "decorative" category into the "folder".\n```\n![screenshot](https://user-images.githubusercontent.com/16024979/134804570-a01138e9-7fc0-4d22-b1b5-c52b3cfcf8a2.png)\n![file structure](https://user-images.githubusercontent.com/16024979/134737874-cc04a42e-5855-4acb-9394-dac08352efee.png)\n\n# Arguments:\n\n```\n<asset_type>      "hdris, textures, models"\n-h, --help        show this help message and exit\n-f, --folder      target download folder.\n-c, --category    category to download.\n-s, --sizes       size(s) of downloaded asset files. eg: 1k 2k 4k\n-o, --overwrite   overwrite if the files already exists. otherwise the current task will be skipped.\n-no, --noimgs     do not download \'preview, render, thumbnail...\' images.\n-it, --iters      amount of iterations.\n-v, --version     show program\'s version number and exit\n```\n\n# To-Do\n-   [ ] Unit Tests\n-   [ ] Progressbar for current download task(s)\n-   [ ] Select the file format to download\n-   [ ] Download a specific asset, "polydown hdris stuttgart_suburbs"\n\n# Requirements\n- Python >3.5\n\n## Dependencies\n- [requests](https://pypi.org/project/requests/)\n- [rich](https://github.com/willmcgugan/rich)\n\n# License\n[MIT](https://github.com/agmmnn/polydown/blob/master/LICENSE)',
    'author': 'Gökçe Merdun',
    'author_email': 'agmmnn@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/agmmnn/polydown',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
