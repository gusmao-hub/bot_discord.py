from discord.ext import commands, tasks
from discord import Intents
from TOKEN import token_oculto
import os
import discord
import random



##################################################################################################################################################################################################################################################################################################################################################################

token = token_oculto
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix="!", help_command=None, intents=intents)


##################################################################################################################################################################################################################################################################################################################################################################

@client.event #trigger comunicação Discord X Bot
async def on_ready(): #função async - on_ready (mostra no console se o bot está ONLINE)
    print(f'{client.user.name} [ON SERVER]') #parametros usados para mostrar o nome do bot
    print(f'Server ID - [{client.user.id}]') #parametros usados para mostrar o ID server


@client.event #trigger
async def on_member_join(member): #função async - on_member_join (mostra uma mensagem de boas vindas para o usario recebendo o parametro do decorator)
    await client.get_channel(839576746293723141).send(f'Bem Vindo {member.mention}!') #await é a resposta que o async solicita neste caso apontando para o canal dando get_channel + ID, usando o parametro de membro como mensagem a ser enviada + usuario

@client.event
async def on_member_remove(member):
    await client.get_channel(839576746293723141).send(f'Foi tarde {member.mention} :) ')


@client.event
async def on_raw_reaction_add(payload):
    msgID = 839576746293723141

    if msgID == payload.message_id:
        member = payload.member
        guild = member.guild

        emoji = payload.emoji.name
        if emoji == '1️⃣':
            role = discord.utils.get(guild.roles, name='cargo1')
        elif emoji == '2️⃣':
            role = discord.utils.get(guild.roles, name='cargo2')
        await member.add.roles(role)


#839901912123310121 - cargo1
#839901942125559849 - cargo2

@client.command(pass_context= True)
async def teste2(ctx):
    embed = discord.Embed(

        title="Teste",
        description="Testando reacoes",
        color= discord.Colour.purple()

    )

    msg = await ctx.send(embed=embed)
    await msg.add_reaction('1️⃣')
    await msg.add_reaction('2️⃣')


@client.command()
async def teste(ctx):
    teste = random.randint(1, 9999)
    await ctx.send(f'Estamos no teste {teste} 🚀')

client.run(token)