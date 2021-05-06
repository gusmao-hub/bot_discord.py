from discord.ext import commands, tasks
from discord import Intents
from TOKEN import token_oculto
import os
import discord
import random

##################################################################################################################################################################################################################################################################################################################################################################

token = token_oculto
#intents = discord.Intents.default()
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!", help_command=None, intents=intents)

##################################################################################################################################################################################################################################################################################################################################################################

@bot.event
async def on_ready():
    print('O pai ta ON!')

@bot.event
async def on_member_join(member):
    await bot.get_channel(839576746293723141).send(f'Testando essa porra buceta peluda {member.mention}')

@bot.command()
async def teste(ctx):
    teste = random.randint(1, 9999)
    await ctx.send(f'Estamos no teste {teste} 🚀')

bot.run(token)