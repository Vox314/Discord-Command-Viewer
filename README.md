<div align="center">

# <img src="https://cdn3.emoji.gg/emojis/6243-blurple-slashcommands.png" width="30px" height="30px" alt="blurple_slashcommands"> Discord Command Viewer

[![GitHub release (latest by date)](https://img.shields.io/github/v/release/Vox314/Discord-Command-Viewer?color=green)](https://github.com/Vox314/Discord-Command-Viewer/releases) [![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/) [![Discord API](https://img.shields.io/badge/Discord%20API-v10-blue.svg)](https://discord.com/developers/docs/change-log)

 <!-- [![Github All Releases](https://img.shields.io/github/downloads/Vox314/Discord-Command-Viewer/total.svg?color=lightgreen)]() -->

**CLI** & **GUI** to view global or private commands from your Discord bot.

![App Screenshot](https://camo.githubusercontent.com/a03d78043e98f16bc4c8b8708087d7b9e5d606bf44fe4e8c8040e7d7f8fb32c7/68747470733a2f2f6d656469612e646973636f72646170702e6e65742f6174746163686d656e74732f3937393734343238313835313939303038362f313132333431393038383436373830343234322f696d6167652e706e673f77696474683d31343638266865696768743d383830)

https://github.com/Vox314/Discord-Command-Viewer/assets/116598880/0841b8ee-8238-475e-ada9-84542a9f08f7

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

### GUI (Recommended)
- **Windows:**
Run `gui.py` using:

```
pythonw gui.py
```
- **Mac / Linux:**
Run `gui.py` using:

```
python gui.py
```

Make sure `main.py` and `.env` are in the same directory as the GUI will not function without them.
If you leave the `GUILD_ID` field empty and press the `Update Command List` button, it will show you the global commands of your Discord Bot.

### CLI:
Run `main.py`, using (further information in terminal): 

```
python main.py --h
```

Make sure `main.py` and `.env` are in the same directory as the CLI will not function without them.
