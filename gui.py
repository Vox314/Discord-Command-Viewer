import tkinter as tk
from main import retrieve_commands, display_commands, GUILD_ID

def update_command_list():
    # Retrieve commands using the retrieve_commands function from main.py
    commands = retrieve_commands(GUILD_ID)

    # Clear the text widget
    command_list.delete("1.0", tk.END)

    # Display the commands in the text widget using the display_commands function from main.py
    command_list.insert(tk.END, display_commands(commands, return_output=True))

    # Make it read / copy only
    command_list.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Discord Command Viewer")

# Create a text widget for displaying the command list
command_list = tk.Text(root)
command_list.pack()

# Create a button to update the command list
update_button = tk.Button(root, text="Update Command List", command=update_command_list)
update_button.pack()

root.mainloop()