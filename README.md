# Automatically open Zotero item link
Python script to watch clipboard for zotero item links and then open them automatically.

Example urls which can be opened: `zotero://select/library/items/T2I7UWWZ`

This is the command which is executed: `/opt/Zotero_linux-x86_64/zotero -p default --url zotero://select/library/items/HBUVUWMT`

# Requirements

On Linux you need to install a copy/paste mechanism (for details see [here](https://pyperclip.readthedocs.io/en/latest/index.html#not-implemented-error)).

In my case on Fedora you can install `xsel` with: `sudo dnf install xsel`. This works also in Qubes OS for the local qube clipboard.

# Note

To copy the zotero item url you need to install the [Zutilo Plugin](https://github.com/willsALMANJ/Zutilo).

Then go to *Tools -> Zutilo Settings -> Shortcuts -> Copy select item links -> CTRL+C*

## To start it

`python main.py --zotero="path to zotero" --profile="profile name"`

The copied item link will only be opened if you have a linebreak at the end to prevent open the link if you copy it from zotero to your destination.