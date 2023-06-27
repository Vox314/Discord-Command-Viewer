<div align="center">

# Discord Command Viewer
<img src="https://cdn3.emoji.gg/emojis/6243-blurple-slashcommands.png" width="32px" height="32px" alt="blurple_slashcommands">

[![GitHub release (latest by date)](https://img.shields.io/github/v/release/Vox314/Discord-Command-Viewer?color=blue)](https://github.com/Vox314/Discord-Command-Viewer/releases) <!-- [![Github All Releases](https://img.shields.io/github/downloads/Vox314/Discord-Command-Viewer/total.svg?color=lightgreen)]() -->

**CLI** & **GUI** to view global or private commands from your Discord bot.

</div>

## Requirements

- [Python3.10](https://www.python.org/downloads/release/python-3100/)

```bash
pip install customtkinter
```

## Setup
You should consider making a `.env` file in the root directory of the project with your Bot's Token.\
(This script will not function without one).

```bash
TOKEN = NzA1MjM0NTY3ODkwMTIzNDU2.Xq3fWg.8dP0hZvFvg9R7jZcZcDmZmZmZmZ
```

**NOTE:**\
The Bot Token above is a dummy Bot Token used only to show an example of how to make the `.env` file.\
Your Bot Token will **not** be shared with any third party while using this script!

## Running:

**GUI (Recommended)**\
Run `gui.py`, make sure `main.py` and `.env` are in the same directory as the GUI will not function without them.
If you leave the `GUILD_ID` field empty and press the `Update Command List` button, it will show you the global commands of your Discord Bot.

**CLI:**\
Run `main.py`, using (furter information in terminal): 

```
python3 main.py --h
```

Make sure `main.py` and `.env` are in the same directory as the CLI will not function without them.