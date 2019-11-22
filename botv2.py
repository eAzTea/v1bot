import discord
from discord.ext import commands
from discord.ext import tasks
from itertools import cycle
import datetime

TOKEN = 'NjQ1MzIzMzI3NDM0NTIyNjU0.XdWg2w.hbxySVRk9p-KFO9mhDpqs_I9EjQ'


client = commands.Bot(command_prefix = ".")

client.remove_command('help')

status = cycle(['by ΞΛZТΞΛ#8177','.helpme','vib.one/teatimemodding','FREE MOD MENUS'])


@client.event
async def on_ready():
    change_status.start()
    print('BOT is ready')


@tasks.loop(seconds=60)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.command()
async def helpme(ctx):
    embed = discord.Embed(title="LIST of COMMANDS", description="----------", color=0xDC14C, timestamp=datetime.datetime.utcnow())

    embed.add_field(name="General Commands", value=".website"

                    "           .status")

    embed.add_field(name="The Prefix is: !", value=f"I am in {len(client.guilds)} Servers")
    embed.add_field(name="HERE is my Invite Link", value="[http://bit.ly/32W8Nr6]")

    embed.set_footer(text=f"Requested by: {ctx.author.name}")

    await ctx.send(embed=embed)

@client.command()
async def website(ctx):
    await ctx.send(f'WEBSITE: https://www.vib.one/teatimemodding/')

@client.command()
async def status(ctx):
    await ctx.send(f'STATUS: https://teatimemodding.wixsite.com/modmenus/status')

client.run(TOKEN)
