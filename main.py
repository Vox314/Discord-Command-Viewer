"""
## DCV (CLI)

Copyright (c) [Vox314](https://github.com/Vox314) \ 
MIT, see LICENSE for more details.

This script retrieves and displays Discord bot commands.

It can retrieve either global commands or private commands for a specific guild, \ 
depending on whether or not a GUILD_ID is provided.

This is the CLI \ 
run gui.py for the GUI
"""

import requests, os, argparse
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('TOKEN')
GUILD_ID = None
OWNER = 'Vox314'
REPO = 'Discord-Command-Viewer'
API_VERSION = 'v10'

version = 'v0.2.2'

class NetworkError(Exception):
    pass

def get_latest_release(owner, repo):
    headers = {
        'Accept': 'application/vnd.github+json'
    }
    url = f'https://api.github.com/repos/{owner}/{repo}/releases/latest'
    try:
        response = requests.get(url, headers=headers)
    except requests.exceptions.RequestException:
        print('Warning: Could not connect to the GitHub API. Using default version: vChip.')
        return 'vChip'

    if response.status_code == 200:
        return response.json()['tag_name']
    else:
        print(f'A GitHub API error occurred: {response.text}')
        return 'vChip'

latest_version = get_latest_release(OWNER, REPO)

if latest_version == version or latest_version == 'vChip':
    new_version = ''
else:
    new_version = f'\n\033[32m{latest_version} is now available!\033[0m\n\n'

def get_bot_user_id():
    try:
        response = requests.get(
            f'https://discord.com/api/{API_VERSION}/users/@me',
            headers={'Authorization': f'Bot {BOT_TOKEN}'}
        )
    except requests.exceptions.RequestException:
        raise NetworkError('Could not connect to the Discord API. Please check your internet connection.')

    if response.status_code == 200:
        return response.json()['id']
    else:
        print(f"A Discord API error occurred: {response.text}")
        return None

def retrieve_commands(guild_id=None):
    if guild_id is not None:
        try:
            guild_id = int(guild_id)
            guilds = f"guilds/{guild_id}/"
        except ValueError or TypeError:
            return "Error: Please enter a valid integer for GUILD_ID."
    else:
        guilds = ""
    
    # Error for GUI text widget
    if 'CLIENT_ID' not in globals():
        return 'Error: Could not retrieve bot user ID. Please check your internet connection and try again.'
    else:
        api_link = f"https://discord.com/api/{API_VERSION}/applications/{CLIENT_ID}/{guilds}commands"

    headers = {
        "Authorization": f"Bot {BOT_TOKEN}"
    }

    try:
        response = requests.get(api_link, headers=headers)
    except requests.exceptions.RequestException:
        raise NetworkError('Could not connect to the Discord API. Please check your internet connection.')

    status = response.status_code
    #print(response.status_code) # Uncomment for debugging
    match status:
        case 200:
            return response.json()
        case 400:
            data = response.json()
            if data.get('code') == 50035:
                return "Error: Please enter a valid snowflake for GUILD_ID"
        case 401:
            data = response.json()
            if "message" in data and data["message"] == "401: Unauthorized":
                return "Error: The request lacks valid authentication credentials."
        case 403:
            return "Error: Bot does not have access to this server."
        case _:
            print(f"An error occurred: {response.text}")
            return "Error: An unknown error occurred."

try:
    CLIENT_ID = get_bot_user_id()
    commands = retrieve_commands(GUILD_ID)
except NetworkError as e:
    print('Error: Could not retrieve bot user ID. Please check your internet connection and try again.')
    print("Error:", e)

def display_commands(commands, args=None, return_output=False):
    output = ""
    if not commands:
        output += "No commands found.\n"
    else:
        if GUILD_ID is not None:
            output += 'Private (Guild) commands:\n'
        elif GUILD_ID is None:
            output += 'Global commands:\n'

        for command in commands:
            # Always display the command name
            output += f"Command name: {command['name']}\n"

            if args is not None and (args.description or args.options or args.id):
                if args.description:
                    output += f"Command description: {command['description']}\n"
                if args.options:
                    if 'options' in command:
                        output += "Command Options:\n"
                        for option in command['options']:
                            output += f"\tName: {option['name']}\n"
                            output += f"\tType: {option['type']}\n"
                            output += f"\tDescription: {option['description']}\n"
                    else:
                        output += "No options found.\n"
                if args.id:
                    output += f"Command ID: {command['id']}\n"
            else:
                output += f"Command description: {command['description']}\n"
                if 'options' in command:
                    output += "Command Options:\n"
                    for option in command['options']:
                        output += f"\tName: {option['name']}\n"
                        output += f"\tType: {option['type']}\n"
                        output += f"\tDescription: {option['description']}\n"
                else:
                    output += "No options found.\n"

                output += f"Command ID: {command['id']}\n"

            # Add a newline character after each command
            output += "\n"

    if return_output:
        return output
    else:
        print(output)

def run(args):
    if args.all and args.guild:
        print("Error: Invalid use of args, only -a or -g can be used at a time.")
        return

    if args.all:
        commands = retrieve_commands()
    else:
        guild_id = args.guild
        commands = retrieve_commands(guild_id)

    if isinstance(commands, str) and commands.startswith("Error:"):
        # An error occurred, display the error message
        print(commands)
    else:
        # No error occurred, display the commands
        display_commands(commands, args) # return_output=False by default (this is to notice if it's for the GUI or CLI)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
    formatter_class=argparse.RawTextHelpFormatter,
    description=f'{new_version}Discord Command Viewer {version}\nRetrieve and display Discord bot commands.'
    )
    parser.add_argument('-a', '--all', action='store_true', help='shows all global / public commands (if any) (on by default unless specifying a GUILD_ID).')
    parser.add_argument('-g', '--guild', type=int, metavar='<GUILD_ID>', help='shows only the private commands of a specific guild (if any).')
    parser.add_argument('-d', '--description', action='store_true', help='shows only command descriptions.')
    parser.add_argument('-o', '--options', action='store_true', help='shows only command options.')
    parser.add_argument('-i', '--id', action='store_true', help='shows only command IDs.')
    args = parser.parse_args()
    run(args)