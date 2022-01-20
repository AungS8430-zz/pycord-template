import discord
from discord.errors import PrivilegedIntentsRequired
from discord.ext import commands, tasks
import os
from discord import Intents, Bot
from keep_alive import keep_alive
from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents.all()
intents.members = True
intents.messages = True

bot=discord.Bot(intents=intents)

for ext in ['cogs.basic.ping']: #add file directory into the list.
    bot.load_extension(ext)

keep_alive() #If you are using Repl.it, this will make your bot online, make sure that you add the mornitor!
bot.run(str(os.environ.get('token')))
