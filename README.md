# Discord Command Viewer

[![GitHub release (latest by date)](https://img.shields.io/github/v/release/Vox314/Discord-Command-Viewer?color=blue)](https://github.com/USERNAME/REPO/releases) [![Github All Releases](https://img.shields.io/github/downloads/Vox314/Discord-Command-Viewer/total.svg?color=lightgreen)]()

**CLI** & **GUI** to view global or private commands from your Discord bot.

## Requirements

- [Python3.10](https://www.python.org/downloads/release/python-3100/)

## Config

Open `main.py` and use following structure;

| Property | Type | Description |
|----------|------|-------------|
| GUILD_ID | `int` | The ID of your Debug Guild, set to `None` to view global commands |

**NOTE:**\
For the GUI to work you can just leave `GUILD_ID` as it is.

## Token:

You should consider making a `.env` file in the root directory of the project with your Bot's Token.\
(This script will not function without one).
```bash
TOKEN = NzA1MjM0NTY3ODkwMTIzNDU2.Xq3fWg.8dP0hZvFvg9R7jZcZcDmZmZmZmZ
```

**NOTE:**\
The Bot Token above is a dummy Bot Token used only to show an example of how to make the `.env` file.\
Your Bot Token will **not** be shared with anyone while using this script!

## Running:

**GUI (Recommended):** Open `gui.py`, make sure `main.py` and `.env` are in the same directory as the GUI cannot function without them.\
If you leave the `GUILD_ID` field empty and press `Update Command List` button, it will show you the global commands.\
**CLI (Not recommended):** Open `main.py`, make sure you setup `.env` in the same direcotry, as the CLI cannot function without it, if you wish to change the `GUILD_ID` you need to change it between executions of the script.\
If you set the value `GUILD_ID` to `None` it will show you the global commands.