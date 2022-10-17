import discord
import api
from api import key
import init

command = "@client.command()"

cooldown = "@commands.cooldown()"

roleholder = "Admin"

rolelock = f"@commands.has_role({roleholder})"

confholder = "conf.placeholder"

commandname = confholder

defhere = f"async def {commandname}(ctx)"

print(f"Config def: {defhere}")
print(f"Api cog loaded, {key}")

