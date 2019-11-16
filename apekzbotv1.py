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
    print('Bot online!')

@client.command()
async def status(ctx):
    await ctx.author.send('Status: https://teatimemodding.wixsite.com/modmenus/status')
@client.command()
async def sc(ctx):
    await ctx.author.send('Add me on Social Club: https://boost.ink/-t1z9')
@client.command()
async def website(ctx):
    await ctx.author.send('Modmenu Website: https://teatimemodding.wixsite.com/modmenus')
@client.command()
async def com(ctx):
    await ctx.author.send('``` BOT COMMANDS: !sc (Send you the Link for my Socialclubname) | !status (Send you the Link to the Status from the Modmenus) | !website(Send you the Link for my Website) ```')
client.run('NjQ1MzIzMzI3NDM0NTIyNjU0.XdBcUg.uj2XQuDd2OurJuKeCyuZebZd2TY')

