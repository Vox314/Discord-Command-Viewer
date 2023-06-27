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

import customtkinter as ctk
from customtkinter import CTkButton as Button
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
            command_list.configure(state=ctk.NORMAL)
            command_list.delete("1.0", ctk.END)
            command_list.insert(ctk.END, "Error: Please enter a valid integer for GUILD_ID.")
            command_list.configure(state=ctk.DISABLED)
            return

    # Retrieve commands using the retrieve_commands function from main.py
    commands = retrieve_commands(GUILD_ID)

    # Clear the text widget
    command_list.configure(state=ctk.NORMAL)
    command_list.delete("1.0", ctk.END)

    if isinstance(commands, str) and commands.startswith("Error:"):
        # An error occurred, display the error message
        command_list.insert(ctk.END, commands)
    else:
        # No error occurred, display the commands ctk
        command_list.insert(ctk.END, display_commands(commands, return_output=True))

    command_list.configure(state=ctk.DISABLED)

def toggle_theme():
    current_mode = ctk.get_appearance_mode()
    if current_mode == 'Dark':
        ctk.set_appearance_mode('Light')
        theme_button.configure(text='Dark Theme')
        if GUILD_ID_entry.get() == "GUILD_ID":
            GUILD_ID_entry.configure(text_color="grey")
        else:
            GUILD_ID_entry.configure(text_color="black")
    else:
        ctk.set_appearance_mode('Dark')
        theme_button.configure(text='Light Theme')
        if GUILD_ID_entry.get() == "GUILD_ID":
            GUILD_ID_entry.configure(text_color="grey")
        else:
            GUILD_ID_entry.configure(text_color="white")

def on_focus_in(event):
    if GUILD_ID_entry.get() == "GUILD_ID":
        GUILD_ID_entry.delete(0, ctk.END)
    current_mode = ctk.get_appearance_mode()
    if current_mode == 'Dark':
        GUILD_ID_entry.configure(text_color="white")
    elif current_mode == 'Light':
        GUILD_ID_entry.configure(text_color="black")

def on_focus_out(event):
    if GUILD_ID_entry.get() == "":
        GUILD_ID_entry.insert(0, "GUILD_ID")
        GUILD_ID_entry.configure(text_color="grey")

# Create a new ctkinter window
root = ctk.CTk()
root.geometry("960x540")
root.title(f"Discord Command Viewer {version}")
root.resizable(False, False)

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

# Create widgets
GUILD_ID_entry = ctk.CTkEntry(root)
GUILD_ID_entry.insert(0, "GUILD_ID")
GUILD_ID_entry.configure(text_color="grey")

command_list = ctk.CTkTextbox(root)
command_list.configure(state=ctk.DISABLED)

update_button = Button(root, text="Update Command List", command=update_command_list)

theme_button = Button(root, text="Toggle Theme", command=toggle_theme)

# Bind events to widgets
GUILD_ID_entry.bind("<FocusIn>", on_focus_in)
GUILD_ID_entry.bind("<FocusOut>", on_focus_out)

# Pack the widgets into the window
GUILD_ID_entry.pack()
command_list.pack()
update_button.pack(padx=20, ) # left of here!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
theme_button.pack()

root.mainloop()