#VERSION: 0.0.1
#CREATOR: Marc13#1627
#Status: Not Working

import discord
import api
from api import key
import init

command = "@client.command()"

cooldown = "@commands.cooldown()"

prefix = "?"

defintents = f"intents = discord.Intents.all() client = commands.Bot(command_prefix ={prefix}, case_insensitive = True, intents = intents)"

roleholder = "Admin"

rolelock = f"@commands.has_role({roleholder})"

confholder = "conf.placeholder"

commandname = confholder

defhere = f"async def {commandname}(ctx)"

event = "@client.event"


print(f"Config def: {defhere}")
print(f"Api cog loaded, {key}")

