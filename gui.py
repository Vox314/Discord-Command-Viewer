"""
## DCV (GUI)

Copyright (c) [Vox314](https://github.com/Vox314) \ 
MIT, see LICENSE for more details.

This script retrieves and displays Discord bot commands.

It can retrieve either global commands or private commands for a specific guild, \ 
depending on whether or not a GUILD_ID is provided.

This is the GUI \ 
run main.py for the CLI
"""

import tkinter as tk
from main import retrieve_commands, display_commands

def update_command_list():
    # Retrieve the value from the Entry widget
    GUILD_ID = int(GUILD_ID_entry.get())

    # Retrieve commands using the retrieve_commands function from main.py
    commands = retrieve_commands(GUILD_ID)

    # Clear the text widget
    command_list.config(state=tk.NORMAL)
    command_list.delete("1.0", tk.END)

    if isinstance(commands, str) and commands.startswith("Error:"):
        # An error occurred, display the error message
        command_list.insert(tk.END, commands)
    else:
        # No error occurred, display the commands
        command_list.insert(tk.END, display_commands(commands, return_output=True))

    # Make it read / copy only
    command_list.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Discord Command Viewer")

# Create an Entry widget for inputting GUILD_ID
GUILD_ID_entry = tk.Entry(root)
GUILD_ID_entry.pack()

# Create a text widget for displaying the command list
command_list = tk.Text(root)
command_list.pack()

# Create a button to update the command list
update_button = tk.Button(root, text="Update Command List", command=update_command_list)
update_button.pack()

root.mainloop()