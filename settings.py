import discord
import random
import requests
import uuid
import yt_dlp
from collections import deque
from discord import FFmpegPCMAudio
from discord.ext import commands
from random import randint
from requests import get
from responses import *
from yt_dlp import YoutubeDL
from on_ready import *

prefix = '123'# - debug prefix
# prefix = '~'
description = 'joonsauce Music Bot v2.0'
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=prefix, intents=intents, description=description)
bot.remove_command('help')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(description))
    print("Status: OK")

players = {}

links = {}

titles = {}

now_playing = {}

now_url = {}

loop_url = {}

loop_title = {}
