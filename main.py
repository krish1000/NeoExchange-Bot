import discord
from discord.ext import tasks
import os
# import requests
# import json
# from replit import db  #, Database , ReplInfo

# import time
from replit import db
### Importing neo scraper
from scraper import Scraper
import neo_db_query as nq
import neo_db_store as ns

intents=discord.Intents.default()  # not sure
intents.message_content = True
intents.messages = True
# intents.

client = discord.Client(intents=intents)
BOT_TOKEN = os.environ['BOT_TOKEN']

scrape = Scraper() # initalize neo scraper from scrape.py

print("created discord client")
bot = {
  'command_prefix': "$neo fetch",
  'initialize_prefix': "$neo set",
}

@tasks.loop(seconds=60)
async def run_batch():
  print('running...')
  
  currData = scrape.fetch_neo_data()
  currNumOfData = len(currData.keys())
  if nq.get_number_of_cdrs() == -1: # cdrs not initialized
    print("NOT INTIALIZED")
    ns.put_number_of_cdrs(currNumOfData)
    ns.put_cdrData(currData)
  elif nq.is_number_of_cdrs_changed(currNumOfData): # new cdr(s) has been found
    print("NEWDATA")
    changedDataSymbs = nq.get_changed_cdrData(currData)
    msg = ""
    for symb in changedDataSymbs:
      msg += ", " + symb
    msg = msg[2:]

    print(msg)
    # Send new cdrs found to each channel for each server
    if "servers" in db.keys():
      servers = db['servers']
      print(servers)
      for server in servers: #for each server, run batch
        channel = client.get_channel(servers[server])
        await channel.send("New CDRs are available: " + msg)
    ns.put_number_of_cdrs(currNumOfData)
    ns.put_cdrData(currData)
  else: #no new cdrs have been found, replace data
    ns.put_cdrData(currData)
  print('completed.')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    run_batch.start()

@client.event
async def on_message(message):
  #checks if msg is by bot, if it is return nothing
    if message.author == client.user:
      return

    if message.content.startswith(bot['command_prefix']):
      try:
        # await message.channel.send("HELLLOO")

        # content = scrape.fetch_neo_data()
        # for i in range(0, content % )
        await message.channel.send(scrape.fetch_neo_data())
      except Exception as e:
        print("ERRROR")
        print(e)
        await message.channel.send("error occured.")

    # Set channel 
    elif message.content.startswith(bot['initialize_prefix']):
              
      serverID = message.guild.id
      print(serverID)

      channelID = message.channel.id
      print(channelID)
      if "servers" in db.keys(): #key exists, thus append to servers
        db["servers"][serverID] = channelID
      else: #key doesnt exist thus create new key and append first server & channel ids
        db["servers"] = {serverID: channelID}
  
      print(db["servers"])
      
    else:
      print(message.content)

client.run(BOT_TOKEN)

