# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['stickytext', 'stickytext.window']

package_data = \
{'': ['*']}

install_requires = \
['pygobject>=3.42.1,<4.0.0', 'setuptools>=67.7.1,<68.0.0']

entry_points = \
{'console_scripts': ['stickytext = stickytext.app:run_app']}

setup_kwargs = {
    'name': 'stickytext',
    'version': '0.1.0',
    'description': 'An extremely simple app for showing a text file as a sticky note',
    'long_description': "# StickyText\n\nThis is an extremely simple app with the only purpose of loading a text file in an editor and syncing any changes between the\neditor and the text file. It is intended to be used as a simple sticky note app to make quick jottings into text files. Additional features such\nas autostarting and resizing, repositioning, and pinning to top, can be achieved by using additional tools.\n\n\n## Usage\n\nExecute the below command in a terminal\n```commandline\npython3 -m stickytext /path/to/textfile.txt\n```\n\nThe app is configured to automatically save any changes as you type and to load any changes should the file be modified\nfrom disk.\n\nFor convenience, any file changes loaded from the disk can be undone using the context menu\n\n\n## Autostart\nStarting the app on login can be achieved by adding an entry in your DE's autostart list\n\n## Size / Position /Always on Top\nTo configure the size and position of the app, as well as to keep it pinned on top, it is recommended to use\ndevilspie2.\n\nAn example configuration is located in this repo as ./stickytext.lua. Simply copy this file to ~/.config/devilspie2 and adjust the window\nname and desired geometry.\n\nAs an alternative, most modern desktop environments have the capability of pinning windows on top and some has the ability to remember the position\nand size of the window.\n\n\n# Use Case\n\nThe following setup allows for a simple synced sticky notes sytem between Android and Linux\n\n1. On your computer, create one or more text files to be used as your sticky notes.\n2. Setup StickyText to autostart and open the text files in a small, always on top window using the above mentioned devilspie2 config.\n3. Sync the text with your phone (e.g. Syncthing, Nextcloud, etc.)\n4. On Android, install [Simple Notes Pro](https://f-droid.org/packages/com.simplemobiletools.notes.pro/) from F-Droid\n5. In Simple Notes, open the text file by using the Open Note menu item.\n6. Create a Notes widget from the Simple Notes app to allow access to the notes on your home screen.\n",
    'author': 'BeatLink',
    'author_email': 'beatlink+git@simplelogin.co',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/BeatLink/StickyText',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
