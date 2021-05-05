from discord.ext import commands, tasks
from TOKEN import token_oculto
import os
import discord
import asyncio
import random

##############################################################################################################################################################################################################################################################################################################################################################################

token = token_oculto
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix="!", help_command=None)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='Bip, Bop i am a Bot :)'))
    print('I am alive.')

@client.event
async def on_member_join(member):
    servidor = client.get_guild(839270176264159233)
    canal = guild.get_channel(839526474955882507)
    await canal.send(f'Testando...{member.mention}')

@client.event
async def on_member_remove(member):
    servidor = client.get_guild(839270176264159233)
    canal = guild.get_channel(839526474955882507)
    await canal.send(f'Testando...{member.mention}')

@bot.command()
async def teste(ctx):
    teste = random.randint(1, 9999)
    await ctx.send(f'Estamos no teste {teste} 🚀')

bot.run(token)