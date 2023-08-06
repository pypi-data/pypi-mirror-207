# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyanide']

package_data = \
{'': ['*']}

install_requires = \
['mdformat', 'mistune', 'tabulate']

setup_kwargs = {
    'name': 'pyanide',
    'version': '1.1.0',
    'description': 'Tools for killing processes and keeping them dead.',
    'long_description': '# pyanide\n\nThis is library helps kill processes. For example, you might be able to exit vim by killing the process, but you may also want to keep it dead by periodically checking to see if it has come back to life and re-killing it.\n\nMore importantly, [it is a library that the people want](https://elk.zone/mastodon.social/@mergesort@macaw.social/110346638073185447).\n\nCreated with help from ChatGPT.\n\n```bash\npython -m pyanide vim\n```\n\n![Libraries.io dependency status for latest release](https://img.shields.io/librariesio/release/pypi/pyanide) [![Downloads](https://pepy.tech/badge/pyanide/month)](https://pepy.tech/project/pyanide/month)\n\n______________________________________________________________________\n\n## Installation\n\n```shell\npip install pyanide\n```\n\n\n## Prior Art\n\n\n## Documentation\n\n- [TODO](https://github.com/matthewdeanmartin/pyanide/blob/main/docs/TODO.md)\n',
    'author': 'Matthew Martin',
    'author_email': 'matthewdeanmartin@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/matthewdeanmartin/pyanide',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
}


setup(**setup_kwargs)
