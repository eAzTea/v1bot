import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(game=Game(name='Rainbow Six'))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content == '$help':
        await client.send_message(message.channel,'Wenn du Neu bist melde dich zuerst bei einen Operator!')
client.run('NTIyNzg5Njc5ODcxODE5Nzg2.DvQFhw.INWP8K064raDypBIw5lw50ztT8M')
