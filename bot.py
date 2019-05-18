import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game



Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'Tere Pede!')
    print('Sent message to ' + member.name)
async def on_ready():
    await client.change_presence(game=Game(name='      '))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content == 'Boss1':
        await client.send_message(message.channel,'Boss on hea olla')
    if message.content == 'Boss':
        em = discord.Embed(description='Bossi statid')
        em.set_image(url='https://cdn.discordapp.com/attachments/554324936827600896/565477941115486219/unknown.png')
        await client.send_message(message.channel, embed=em)
    if message.content == 'Kaur':
        await client.send_message(message.channel,'Kaur on tore poiss')
    if message.content == 'Pro':
        await client.send_message(message.channel,'@everyone Robin on noob')
    if message.content == '@everyone Robin on noob':
        await client.send_message(message.channel,'Ahahahaha')
    if message.content == 'Reeglid':
        await client.send_message(message.channel,'1.kui tahad ramonit solvata kirjuta Pro')
    if message.content == '1.kui tahad ramonit solvata kirjuta Pro':
        await client.send_message(message.channel,'2.Ära spamma')
    if message.content == '2.Ära spamma':
        await client.send_message(message.channel,'3.Ära sega Kauri ')
    if message.content == '3.Ära sega Kauri ':
        await client.send_message(message.channel,'4.Spammake Robinit,rampoui,spammer')
    if message.content == 'Hoiatus':
        await client.send_message(message.channel,'Ramon sai hoiatuse')
    if message.content == 'ramon':
        await client.send_message(message.channel,'Ramon sai suure paksu hoitatuse')
    if message.content == 'Noob':
        await client.send_message(message.channel,'Kaur on pro')
    if message.content == 'Kicklol':
        await client.send_message(message.channel,' x!Kick 460161597294379029 TEST')
    if message.content == '!taun':
        await client.send_message(message.channel,'Ramon on taun')
    if message.content == 'Robin':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/566320711660994603/566320751779512320/Hoiva.PNG')
        await client.send_message(message.channel, embed=em)
    if message.content.upper().startswith('!AMIADMIN'):
        if "553180812170756113" in [role.id for role in message.author.roles]: #Replace <Role ID> with the ID of the role you want to be able to execute this command
            await client.send_message(message.channel, "You are an admin")
        else:
            await client.send_message(message.channel, "You are not an admin")
            
    if message.content.upper().startswith('STOP'):
        if "553180812170756113" in [role.id for role in message.author.roles]: #Replace <Role ID> with the ID of the role you want to be able to execute this command
            await client.send_message(message.channel, "@everyone RAMON KIUSAB MIND")
        else:
            await client.send_message(message.channel, "KÜSI MARKUSELT LUBA")
            
    
    


client.run('NTY1NDc4NzgxODc2MTc0ODQ4.XK3FWA.q-OTOU3GUMMFES2eHm70faKFULM')
