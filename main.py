from discord.ext import commands, tasks
from TOKEN import token_oculto
import os
import discord
import asyncio
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
    print('I am alive.')


@client.event
async def on_member_join(members):
    await client.get_channel(839576746293723141)
    print(f'Teste{members.mention}')


@bot.command()
async def teste(ctx):
    teste = random.randint(1, 9999)
    await ctx.send(f'Estamos no teste {teste} 🚀')

bot.run(token)