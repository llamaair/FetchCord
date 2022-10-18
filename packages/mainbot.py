import discord
from discord.ext.commands import bot
from discord.ext import tasks
from discord.ext import commands
import os


command = "@client.command()"

cooldown = "@commands.cooldown()"

slashdesc = "Placeholder"

slash=f"@client.command(description={slashdesc})"

prefix = "?"

defintents = f"intents = discord.Intents.all() client = commands.Bot(command_prefix ={prefix}, case_insensitive = True, intents = intents)"

roleholder = "Admin"

rolelock = f"@commands.has_role({roleholder})"

confholder = "conf.placeholder"

#If you use "replit", create a secret called TOKEN, and set the value to the bot token.
token = os.environ['TOKEN']

commandname = confholder

defhere = f"async def {commandname}(ctx):"

event = "@client.event"


intents = discord.Intents.all()
client = commands.Bot(command_prefix = f"{prefix}" , case_insensitive = True, intents = intents)
client.remove_command('help')

@client.event
async def on_ready():
  print("{0.user} is now online!".format(client))
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{prefix}help"))

@client.command()
async def ping(ctx):
  await ctx.reply("Pong!")

client.run(token)