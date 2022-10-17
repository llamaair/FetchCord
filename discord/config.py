#VERSION: 0.0.1
#CREATOR: Marc13#1627
#Status: Not Working

import discord
from discord import api
from discord import init

command = "@client.command()"

cooldown = "@commands.cooldown()"

prefix = "?"

defintents = f"intents = discord.Intents.all() client = commands.Bot(command_prefix ={prefix}, case_insensitive = True, intents = intents)"

roleholder = "Admin"

rolelock = f"@commands.has_role({roleholder})"

confholder = "conf.placeholder"

commandname = confholder

defhere = f"async def {commandname}(ctx):"

event = "@client.event"


print(f"Config def: {defhere}")

