from TOKEN import token_oculto   ##Token upado separado.
from discord.embeds import Embed
from discord.ext import commands, tasks
from discord import Intents, Colour
import aiohttp
import discord
import random
import os
import youtube_dl

token = token_oculto
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix="!", intents=intents)

async def on_ready(): 
    print(f'{client.user.name} [ON SERVER]')
    print(f'Server ID - [{client.user.id}]')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('!comandos'))

@client.event
async def on_member_join(member): 
    embed = discord.Embed(

        title='Seja bem vindo 😜' ,
        description= member.mention,
        color= discord.Colour.red()
    )
    await member.create_dm()
    await member.dm_channel.send(embed=embed)

@client.event
async def on_member_remove(member):
    embed = discord.Embed(

        title='Foi embora 😔' ,
        description= member.mention,
        color= discord.Colour.red()
    )
    await member.create_dm()
    await member.dm_channel.send(embed=embed)

'''@client.command(pass_context= True) 
async def teste2(ctx):
    embed = discord.Embed(  

        title="Teste de Reações",  
        description="Teste a Reação abaixo",  
        color= discord.Colour.purple() 
    ) 
    msg = await ctx.send(embed=embed) 
    await msg.add_reaction('1️⃣')  
    await msg.add_reaction('2️⃣')  

@client.event                                                           #Não vou usar isso agora.
async def on_raw_reaction_add(payload):
    msg_fixada = payload.message_id    
    if msg_fixada == 841478314848813056:    
        guild_id = payload.guild_id    
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)
        member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)    
        emoji = payload.emoji.name    

        if emoji == '1️⃣':
            role = discord.utils.get(guild.roles, name= 'cargo1')
            await member.add_roles(role) 
        elif emoji == '2️⃣':
            role = discord.utils.get(guild.roles, name= 'cargo2')
            await member.add_roles(role)'''

@client.command()
async def comandos(ctx):
    embed = discord.Embed(
        title= 'Lista de Comandos:',
        description= '!teste 🚀\n !cafe ☕\n !ola 👋 \n !gatinho 😺 \n !d20 🎲 \n !moeda 🕹️ \n',
        color= discord.Colour.red()       
    )
    await ctx.send(embed=embed)

@client.command()
async def d20(ctx):
    dado = random.randint(1,20)
    await ctx.send(f'Você rolou um {dado}')

@client.command()
async def cafe(ctx):
    await ctx.send('Pausa para o ☕')

@client.command()
async def bot(ctx):
    await ctx.send(f'Oie eu sou o bot criado pelo Gusmão espero te ajudar 🧐')

@client.command()
async def moeda(ctx):
    flip = random.randint(1,2)

    if flip == 1:
        await ctx.send(f'Deu 😶')
    elif flip == 2:
        await ctx.send(f'Deu 👑')

@client.command()
async def gatinho(ctx):
    async with ctx.channel.typing():
        async with aiohttp.ClientSession() as cs: #aiohttp.ClientSession() é -> cs
            async with cs.get('http://aws.random.cat/meow') as request: #cs.get + URL é -> request
                data = await request.json()

                embed = discord.Embed(title='🐱')
                embed.set_image(url=data['file'])
                await ctx.send(embed=embed)

client.run(token)
