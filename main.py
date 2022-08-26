import discord
import os
# import requests
# import json
# from replit import db  #, Database , ReplInfo

### Importing neo scraper
from scraper import Scraper

intents=discord.Intents.default()  # not sure
intents.message_content = True
intents.messages = True
# intents.

client = discord.Client(intents=intents)
BOT_TOKEN = os.environ['BOT_TOKEN']

scrape = Scraper() # initalize neo scraper from scrape.py

print("created discord client")
bot = {
    'command_prefix': "$neo",
}

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  #checks if msg is by bot, if it is return nothing
    if message.author == client.user:
      return

    if message.content.startswith(bot['command_prefix']):
      try:
        # await message.channel.send("HELLLOO")
        await message.channel.send(scrape.fetch_neo_data())
      except Exception as e:
        print("ERRROR")
        print(e)
        await message.channel.send("error occured.")
    else:
      print(message.content)

client.run(BOT_TOKEN)

