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

import customtkinter as ctk, os, subprocess, sys
from customtkinter import CTkButton as Button, filedialog
from tkinter import messagebox
from main import retrieve_commands, display_commands, version, latest_version, OWNER, REPO

# This enables or disabled Developer mode. 
DEV_MODE = 0 # 0 = Disabled | 1 = Enabled 

def update_command_list():

    # 1000ms timeout to prevent API spam
    update_button.configure(state='disabled')
    root.after(1000, lambda: update_button.configure(state='normal'))

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

def export_text():
    default_file_name = "DCV-Export"
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    filetypes = [("Text Files", "*.txt")]
    file_path = filedialog.asksaveasfilename(
        initialdir=downloads_folder, initialfile=default_file_name, defaultextension=".txt", filetypes=filetypes, title=f"Discord Command Viewer {version} - Exporter"
        )
    if file_path:
        with open(file_path, 'w', encoding="utf-8") as file:
            text = command_list.get("1.0", "end-1c")
            file.write(text)

# Create a new ctkinter window
root = ctk.CTk()
root.iconbitmap('./assets/icon.ico')
root.title(f"Discord Command Viewer {version}")
root.geometry("960x540") # Default 960x540
root.resizable(False, False)

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

# Create widgets
GUILD_ID_entry = ctk.CTkEntry(root, justify="center")
GUILD_ID_entry.insert(0, "GUILD_ID")
GUILD_ID_entry.configure(text_color="grey")

command_list = ctk.CTkTextbox(root)
command_list.configure(state=ctk.DISABLED)

# Create frame for buttons
button_frame = ctk.CTkFrame(root)

update_button = Button(button_frame, text="Update Command List", command=update_command_list)
theme_button = Button(button_frame, text="Toggle Theme", command=toggle_theme)
export_button = Button(button_frame, text="Export", command=export_text)

# Bind events to widgets
GUILD_ID_entry.bind("<FocusIn>", on_focus_in)
GUILD_ID_entry.bind("<FocusOut>", on_focus_out)

# Pack the widgets into the window
GUILD_ID_entry.pack(fill='x', padx=300, pady=10)
command_list.pack(fill='both', expand=True, padx=20, pady=0)
update_button.pack(side='left', padx=10, pady=10)
theme_button.pack(side='left', padx=10, pady=10)
export_button.pack(side='left', padx=10, pady=10)
button_frame.pack(anchor="center")

RESTART_FLAG = 'SCRIPT_RESTART_FLAG'

if __name__ == "__main__":
    
    if os.environ.get(RESTART_FLAG):
        # The script was restarted after an update
        del os.environ[RESTART_FLAG]
        messagebox.showinfo('Update Successful!', f'The script has been updated to version {version}.')
    
    if latest_version == version or latest_version == 'vChip' or DEV_MODE == 1:
        new_version = ''
    else:
        if DEV_MODE == 0:

            new_version = latest_version
            root.update()

            if messagebox.askquestion('Update Available!', f'{new_version} is available.\nWould you like to install it now?') == 'yes':
                try:
                    # Replace 'username' and 'reponame' with the appropriate values for the GitHub repository
                    subprocess.check_call(['git', 'clone', f'https://github.com/{OWNER}/{REPO}.git']) # FIX THIS SHIT NEED TO CLONE VERSIONS NOT REPOSITORY
                    print("Repository downloaded successfully")
                    
                    # Set the restart flag and restart the script
                    os.environ[RESTART_FLAG] = '1'
                    os.execv(sys.executable, ['python'] + sys.argv)
                except subprocess.CalledProcessError:
                    print("An error occurred while downloading the repository")

        else:
            print(f"DEV_MODE was set to {DEV_MODE}, please use 0 or 1!")

    root.mainloop()