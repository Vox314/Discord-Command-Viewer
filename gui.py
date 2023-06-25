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
from tkinter import ttk
from main import retrieve_commands, display_commands, version

def update_command_list():
    # Retrieve the value from the Entry widget
    GUILD_ID = GUILD_ID_entry.get()
    if GUILD_ID == "" or GUILD_ID == "GUILD_ID":
        GUILD_ID = None
    else:
        try:
            GUILD_ID = int(GUILD_ID)
        except ValueError or TypeError:
            # The value entered by the user is not a valid integer
            command_list.config(state=tk.NORMAL)
            command_list.delete("1.0", tk.END)
            command_list.insert(tk.END, "Error: Please enter a valid integer for GUILD_ID.")
            command_list.config(state=tk.DISABLED)
            return

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

# Create a new Tkinter window
root = tk.Tk()
root.title(f"Discord Command Viewer {version}")

# Create an Entry widget for inputting GUILD_ID
GUILD_ID_entry = tk.Entry(root)
GUILD_ID_entry.insert(0, "GUILD_ID")
GUILD_ID_entry.configure(foreground="grey")

# Bind the focus event to clear the placeholder text when the Entry widget receives focus
def on_focus_in(event):
    if GUILD_ID_entry.get() == "GUILD_ID":
        GUILD_ID_entry.delete(0, tk.END)
        GUILD_ID_entry.configure(foreground="black")

GUILD_ID_entry.bind("<FocusIn>", on_focus_in)

# Bind the focus out event to restore the placeholder text when the Entry widget loses focus
def on_focus_out(event):
    if GUILD_ID_entry.get() == "":
        GUILD_ID_entry.insert(0, "GUILD_ID")
        GUILD_ID_entry.configure(foreground="grey")

GUILD_ID_entry.bind("<FocusOut>", on_focus_out)

# Create a text widget for displaying the command list
command_list = tk.Text(root)
command_list.config(state=tk.DISABLED)

# Create a button to update the command list
update_button = tk.Button(root, text="Update Command List", command=update_command_list)

# Pack the widgets into the window
GUILD_ID_entry.pack()
command_list.pack()
update_button.pack()

root.mainloop()