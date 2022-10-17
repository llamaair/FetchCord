import discord
import asyncio
import random
import time
import datetime
import string
import os
import json
from discord.ext import commands
from discord.ext import tasks
from discord.ext.commands import check
import api.py
import db.json



intents = discord.Intents.all()

client = discord.Bot(intents=intents, help_command=None)

