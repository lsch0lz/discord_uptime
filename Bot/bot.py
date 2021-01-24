# bot.py
import os
import csv
import pandas as pd

import discord
from discord import Status
from dotenv import load_dotenv
from datetime import datetime, date

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
    
    if message.content == '!uptime':
        print(message.author)
        #start_session = get_timediffrence(message.author)
        start_session = "test"
        
        await message.channel.send(str(start_session))
        
@client.event
async def on_member_update(before, after):
    if str(before.status) == "online":
        print("{} has gone {}.".format(before.name,before.status))
        start_time(before.name)

        if str(after.status) == "offline":
            print("{} has gone {}.".format(after.name,after.status))
            end_time(before.name)

            
#functions for timediffrence
def get_timediffrence(author):
    df_start = pd.read_csv("start_time.csv")
    df_end = pd.read_csv("end_time.csv")

    start = df_start[author]
    return start

#logging for the time events
def start_time(author):
    now = datetime.now()
    today = date.today()

    start_time = now.strftime("%H:%M:%S")
    start_date = today.strftime("%d/%m/%Y")

    var = []
    var.append(author)
    var.append(start_time)
    var.append(start_date)

    with open("start_time.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow(var)
   

def end_time(author):
    now = datetime.now()
    today = date.today()

    end_time = now.strftime("%H:%M:%S")
    end_date = today.strftime("%d/%m/%Y")

    var = []
    var.append(author)
    var.append(end_time)
    var.append(end_date)

    with open("end_time.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow(var)

client.run(TOKEN)