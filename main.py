# main.py

"""
This script retrieves and displays Discord bot commands.

It can retrieve either global commands or private commands for a specific guild,
depending on whether or not a GUILD_ID is provided.
"""

import requests, os
from dotenv import load_dotenv

load_dotenv()

# Replace this value with your bot's token (if no .env file is provided)
BOT_TOKEN = os.getenv('token') # The bot's token, retrieved from an environment variable named "token"
GUILD_ID = 1114959767715184730 # None # The ID of the guild for which to retrieve private commands (if any). Set to None to retrieve global commands.

def get_bot_user_id():
    """Retrieve the bot's user ID using its token."""
    response = requests.get(
        'https://discord.com/api/v9/users/@me',
        headers={'Authorization': f'Bot {BOT_TOKEN}'}
    )

    if response.status_code == 200:
        return response.json()['id']
    else:
        print(f"An error occurred: {response.text}")
        return None

CLIENT_ID = get_bot_user_id()

def retrieve_commands(guild_id=None):
    """Retrieve Discord bot commands.

    If a guild_id is provided, retrieve private commands for that guild.
    Otherwise, retrieve global commands.

    Returns a list of commands.
    """
    if guild_id is not None:
        guilds = f"guilds/{guild_id}/"
    else:
        guilds = ""

    api_link = f"https://discord.com/api/v9/applications/{CLIENT_ID}/{guilds}commands"

    headers = {
        "Authorization": f"Bot {BOT_TOKEN}"
    }

    # Print the API link being used
    #print(f"API link: {api_link}")

    response = requests.get(api_link, headers=headers)

    # Print the response received from the API
    #print(f"API response: {response.text}")

    if response.status_code == 200:
        return response.json()
    else:
        print(f"An error occurred: {response.text}")
        return []

def display_commands(commands, return_output=False):
    """Display a list of Discord bot commands."""
    output = ""
    if not commands:
        output += "No commands found.\n"
    else:
        if GUILD_ID is not None:
            output += 'Private (Guild) commands:\n'
        elif GUILD_ID is None:
            output += 'Global commands:\n'

        for command in commands:
            output += f"{command['name']}: {command['id']}\n"
    if return_output:
        return output
    else:
        print(output)

if __name__ == '__main__':

    commands = retrieve_commands(GUILD_ID)
    display_commands(commands) # return_output=False by default