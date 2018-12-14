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
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'Was geht, willkommen bei Apekz. Melde dich zuerst bei einen Operator er wird dir alles weitere erklären!')
    print('Sent message to ' + member.name)
async def on_ready():
    await client.change_presence(game=Game(name='      '))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content == '$avatar':
        await client.send_message(message.channel,'https://cdn.discordapp.com/attachments/520952616843214858/523275442334203915/Apexz_Avatar.png?width=676&height=676')
    if message.content == '$logo':
        await client.send_message(message.channel,'https://cdn.discordapp.com/attachments/520952616843214858/523275401829810186/Apexz_Logo.png')
