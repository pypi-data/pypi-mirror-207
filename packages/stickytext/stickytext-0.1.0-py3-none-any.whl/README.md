# StickyText

This is an extremely simple app with the only purpose of loading a text file in an editor and syncing any changes between the
editor and the text file. It is intended to be used as a simple sticky note app to make quick jottings into text files. Additional features such
as autostarting and resizing, repositioning, and pinning to top, can be achieved by using additional tools.


## Usage

Execute the below command in a terminal
```commandline
python3 -m stickytext /path/to/textfile.txt
```

The app is configured to automatically save any changes as you type and to load any changes should the file be modified
from disk.

For convenience, any file changes loaded from the disk can be undone using the context menu


## Autostart
Starting the app on login can be achieved by adding an entry in your DE's autostart list

## Size / Position /Always on Top
To configure the size and position of the app, as well as to keep it pinned on top, it is recommended to use
devilspie2.

An example configuration is located in this repo as ./stickytext.lua. Simply copy this file to ~/.config/devilspie2 and adjust the window
name and desired geometry.

As an alternative, most modern desktop environments have the capability of pinning windows on top and some has the ability to remember the position
and size of the window.


# Use Case

The following setup allows for a simple synced sticky notes sytem between Android and Linux

1. On your computer, create one or more text files to be used as your sticky notes.
2. Setup StickyText to autostart and open the text files in a small, always on top window using the above mentioned devilspie2 config.
3. Sync the text with your phone (e.g. Syncthing, Nextcloud, etc.)
4. On Android, install [Simple Notes Pro](https://f-droid.org/packages/com.simplemobiletools.notes.pro/) from F-Droid
5. In Simple Notes, open the text file by using the Open Note menu item.
6. Create a Notes widget from the Simple Notes app to allow access to the notes on your home screen.
