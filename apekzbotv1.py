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
    await client.change_presence(game=Game(name='Rainbow Six Siege'))
    await client.send_message(member, 'Willkommen bei Apekz, melde dich bitte zuerst bei einen Operator er wird die weiters erklären! Wenn keiner Online ist dann bitte bei der Leitung! Operator: Lunar_Berry & Hiem | Leitung: eAzTeA & Karuukan')
    print('Sent message to ' + member.name)
async def on_ready():
    await client.change_presence(game=Game(name='      '))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content == '$help':
        await client.send_message(message.channel,'Commands: $avatar ; $logo ; $binneu')
    if message.content == '$logo':
        await client.send_message(message.channel,'https://cdn.discordapp.com/attachments/520952616843214858/523275401829810186/Apexz_Logo.png')
    if message.content == '$avatar':
        await client.send_message(message.channel,'https://cdn.discordapp.com/attachments/520952616843214858/523275442334203915/Apexz_Avatar.png')
    if message.content == '$binneu':
        await client.send_message(message.channel,'Wenn du Neu bist melde dich zuerst bei einen Operator!')
client.run('NTIyNzg5Njc5ODcxODE5Nzg2.DvZ6YA.NznqWz7Gm2ce2FWpD-hXu_7HN_s')

