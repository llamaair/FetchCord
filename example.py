import discimports
from config import defintents
from config import event
import discord
from discord.ext import commands


Token="Token"

str(defintents)

str(event)

print("{0.user} is now online!".format(client))
  await client.change_presence(activity=discord.Activity(
  type=discord.ActivityType.listening, name="?hotspots"))