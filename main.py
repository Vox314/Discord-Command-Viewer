"""
This script retrieves and displays Discord bot commands.

It can retrieve either global commands or private commands for a specific guild,
depending on whether or not a GUILD_ID is provided.
"""

import requests, os
from dotenv import load_dotenv

load_dotenv()

# Replace these values with your bot's information
BOT_TOKEN = os.getenv('token') # The bot's token, retrieved from an environment variable named "token"
CLIENT_ID = 1121059957916323910 # The bot's client ID
GUILD_ID = None # The ID of the guild for which to retrieve private commands (if any). Set to None to retrieve global commands.

if GUILD_ID is not None:
    guilds = f"guilds/{GUILD_ID}/"
else:
    guilds = ""

api_link = f"https://discord.com/api/v9/applications/{CLIENT_ID}/{guilds}commands"

headers = {
    "Authorization": f"Bot {BOT_TOKEN}"
}

if GUILD_ID is not None:
    print('Private (Guild) commands:')
elif GUILD_ID is None:
    print('Global commands:')

response = requests.get(api_link, headers=headers)

if response.status_code == 200:
    commands = response.json()
    if not commands:
        print("No commands found.")
    else:
        for command in commands:
            print(f"{command['name']}: {command['id']}")
else:
    print(f"An error occurred: {response.text}")