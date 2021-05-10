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
async def on_ready(): 
    print(f'{client.user.name} [ON SERVER]')
    print(f'Server ID - [{client.user.id}]')

    #função async - on_ready (mostra no console se o bot está ONLINE)
    #parametros usados para mostrar o nome do bot
    #parametros usados para mostrar o ID server

@client.event #trigger comunicação Discord X Bot
async def on_member_join(member): 
    await client.get_channel(839576746293723141).send(f'Bem Vindo {member.mention}!') 

    #função async - on_member_join (mostra uma mensagem de boas vindas para o usario recebendo o parametro do decorator)
    #await é a resposta que o async solicita neste caso apontando para o canal dando get_channel + ID, usando o parametro de membro como mensagem a ser enviada + usuario

@client.event
async def on_member_remove(member):
    await client.get_channel(839576746293723141).send(f'Foi tarde {member.mention} :)')

    #função async - on_member_remove (mostra uma mensagem de adeus para o usario recebendo o parametro do decorator)
    #await é a resposta que o async solicita neste caso apontando para o canal dando get_channel + ID, usando o parametro de membro como mensagem a ser enviada + usuario

@client.command(pass_context= True) #aqui livra do ctx pra mensagem só passar
async def teste2(ctx): #async é o metodo a ser chamado esperando o contexto
    embed = discord.Embed(  

        title="Teste de Reações",   #titulo da box
        description="Teste a Reação abaixo", #descricao da box
        color= discord.Colour.purple()  #cor da barra lateral

    ) #embed ele permite a edicao da box de mensagem

    msg = await ctx.send(embed=embed)  #await é o que o bot responde
    await msg.add_reaction('1️⃣')  #a mensagem com o simbolo a ser adicionado
    await msg.add_reaction('2️⃣')  #a mensagem com o simbolo a ser adicionado

@client.event
async def on_raw_reaction_add(payload):
    msg_fixada = payload.message_id     #atribuindo o payload a mensagem fixada
    if msg_fixada == 841389681408737301:   #atribuindo o ID da msg marcada
        guild_id = payload.guild_id    #variavel marcando guild_id -> payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)   #variavel marcando guild -> usando lambda func com guild_id/client.guild
        member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)  #variavel marcando member -> usando lambda func com payload.user_id/guild.member
        emoji = payload.emoji.name  #variavel usando emoji react em cima -> usando o payload

        if emoji == '1️⃣':
            role = discord.utils.get(guild.roles, name= 'cargo1')
            await member.add_roles(role)
        elif emoji == '2️⃣':
            role = discord.utils.get(guild.roles, name= 'cargo2')
            await member.add_roles(role)

# variaveis acima para definir roles

@client.command()
async def teste(ctx):
    teste = random.randint(1, 9999)
    await ctx.send(f'Estamos no teste {teste} 🚀')

@client.command()
async def cafe(ctx):
    await ctx.send(f'Pausa para o ☕')

@client.command()
async def ola(ctx):
    await ctx.send(f'Ola seu corno :) tb te amo <3')


client.run(token)