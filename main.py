from discord.ext import commands, tasks
from TOKEN import token_oculto
import os
import discord
import random

##################################################################################################################################################################################################################################################################################################################################################################

token = token_oculto
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix="!", help_command=None)

##################################################################################################################################################################################################################################################################################################################################################################

@client.event
async def on_ready():
    print('O pai ta ON!')


@client.event
async def on_member_join(member):
    await client.get_channel('839576746293723141')
    print(f'Teste')

@client.event
async def on_member_remove(members):
    await client.get_channel('839576746293723141')
    print(f'Teste')

@bot.command()
async def teste(ctx):
    teste = random.randint(1, 9999)
    await ctx.send(f'Estamos no teste {teste} 🚀')

bot.run(token)