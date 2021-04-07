import re
import random
import discord
from discord.ext import commands, tasks

bot = commands.Bot(command_prefix='~')
bot.remove_command('help')
TOKEN = '*V;Yzf(WL(8MV]ae+rh,i{vMP}tP}uwT8_-LC$3z5eTdVb3fY)Bk:yhtV,Q'

@bot.event
async def on_ready():
    print("Cool")

@bot.command()
async def help(ctx):
    await ctx.send('''```
~~~~~~~~~~~Help~~~~~~~~~~~
~help -> Help menu
~~~~~~~~~~~~~~~~~~~~~~~~~~
```''')

bot.run(TOKEN)
