from discord.ext import commands, tasks
from discord import Intents, colour
from TOKEN import token_oculto
import aiohttp
import discord
import random

token = token_oculto
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix="!", help_command=None, intents=intents)

async def on_ready(): 
    print(f'{client.user.name} [ON SERVER]')
    print(f'Server ID - [{client.user.id}]')

    #função async - on_ready (mostra no console se o bot está ONLINE)
    #parametros usados para mostrar o nome do bot
    #parametros usados para mostrar o ID server

@client.event #trigger comunicação Discord X Bot
async def on_member_join(member): 
    await client.get_channel(839576746293723141).send(f'Seja bem vindo :) {member.mention}') 

    #função async - on_member_join (mostra uma mensagem de boas vindas para o usario recebendo o parametro do decorator)
    #await é a resposta que o async solicita neste caso apontando para o canal dando get_channel + ID, usando o parametro de membro como mensagem a ser enviada + usuario

@client.event
async def on_member_remove(member):
    await client.get_channel(839576746293723141).send(f'Foi tarde {member.mention} :)')

    #função async - on_member_remove (mostra uma mensagem de adeus para o usario recebendo o parametro do decorator)
    #await é a resposta que o async solicita neste caso apontando para o canal dando get_channel + ID, usando o parametro de membro como mensagem a ser enviada + usuario

@client.command(pass_context= True) #pass_context = Não faço ideia do porque mas precisa estar como TRUE
async def teste2(ctx): #comando criado que vai ser chamado com o prefixo >!<
    embed = discord.Embed(  

        title="Teste de Reações",  #titulo da box
        description="Teste a Reação abaixo",  #descricao da box
        color= discord.Colour.purple()  #cor da barra lateral

    ) #embed ele permite a edicao da box de mensagem

    msg = await ctx.send(embed=embed)  #Await retorno da mensagem com a edição de embed
    await msg.add_reaction('1️⃣')  #Mensagem com a react.
    await msg.add_reaction('2️⃣')  #Mensagem com a react.

@client.event
async def on_raw_reaction_add(payload):
    msg_fixada = payload.message_id    #Atribuindo msg_fixada ao método payload.message_id
    if msg_fixada == 841478314848813056:    #Atribuindo msg_fixada ao ID da mensagem fixada no canal
        guild_id = payload.guild_id    #Atribuindo guild_id ao método payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)    #Atribuindo a VAR guild aos métodos discord.utils.find com os seus parametros
        member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)    #Atribuindo VAR member aos métodos discord.utils.find com os seus parametros
        emoji = payload.emoji.name    #Atribuindo a VAR emoji aos métodos payload.emoji.name

        if emoji == '1️⃣':   #Utilizando a mensagem com embed aplicado esperando a reação [1]
            role = discord.utils.get(guild.roles, name= 'cargo1') #VAR role aplicando os metodos do discord.utils.get(parametros de guild.role, name = nome do cargo)
            await member.add_roles(role) #Await vai adicionar o membro na role de reação [1]
        elif emoji == '2️⃣': #Utilizando a mensagem com embed aplicado esperando a reação [2]
            role = discord.utils.get(guild.roles, name= 'cargo2') #VAR role aplicando os metodos do discord.utils.get(parametros de guild.role, name = nome do cargo)
            await member.add_roles(role) #Await vai adicionar o membro na role de reação [2]

# variaveis acima para definir roles

#################################################################################################################################################################################
#################################################################### - [ Lista de Comandos abaixo] - ############################################################################
#################################################################################################################################################################################

@client.command()
async def help(ctx):
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
async def teste(ctx):
    teste = random.randint(1, 9999)
    await ctx.send(f'Estamos no teste {teste} 🚀')

@client.command()
async def cafe(ctx):
    await ctx.send('Pausa para o ☕')

@client.command()
async def bot(ctx):
    await ctx.send(f'Posso ser um bot mas pelo menos não sou gado.')

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
            async with cs.get('http://aws.random.cat/meow') as request: #cs.get + URL é ->
                data = await request.json()

                embed = discord.Embed(title='🐱')
                embed.set_image(url=data['file'])
                await ctx.send(embed=embed)
        
client.run(token)
