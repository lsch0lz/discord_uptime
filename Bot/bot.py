# bot.py
import os

import discord
from discord import Status
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.all()
intents.members = True


client = discord.Client(intents=intents)

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes =  'I\'m the human form of the 💯 emoji.'
        
        

    if message.content == '!99':
        response = brooklyn_99_quotes
        await message.channel.send(response)

@client.event
async def on_member_update(before, after):
    if str(before.status) == "online":
        print("{} has gone {}.".format(before.name,before.status))
        
        if str(after.status) == "offline":
            print("{} has gone {}.".format(after.name,after.status))


client.run(TOKEN)