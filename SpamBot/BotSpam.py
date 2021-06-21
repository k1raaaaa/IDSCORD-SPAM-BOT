import colorama
from colorama import Fore
import discord
import time
print(Fore.MAGENTA + """

 ▄▄▄▄    ▒█████  ▄▄▄█████▓     ██████  ██▓███   ▄▄▄       ███▄ ▄███▓
▓█████▄ ▒██▒  ██▒▓  ██▒ ▓▒   ▒██    ▒ ▓██░  ██▒▒████▄    ▓██▒▀█▀ ██▒
▒██▒ ▄██▒██░  ██▒▒ ▓██░ ▒░   ░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▓██    ▓██░
▒██░█▀  ▒██   ██░░ ▓██▓ ░      ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██    ▒██ 
░▓█  ▀█▓░ ████▓▒░  ▒██▒ ░    ▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒██▒   ░██▒
░▒▓███▀▒░ ▒░▒░▒░   ▒ ░░      ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ░  ░
▒░▒   ░   ░ ▒ ▒░     ░       ░ ░▒  ░ ░░▒ ░       ▒   ▒▒ ░░  ░      ░
 ░    ░ ░ ░ ░ ▒    ░         ░  ░  ░  ░░         ░   ▒   ░      ░   
 ░          ░ ░                    ░                 ░  ░       ░   
      ░                                                             

""")
print(Fore.RED + "Bot create by Zerfox | Discord: ─=≡Σ((( つ◕ل͜◕)つ#0021")
print(Fore.YELLOW + "my github is https://github.com/pommepoirechocolat/")




import discord,os,asyncio
from discord.ext import commands, tasks
    
tokenraid = input ("\n\nToken du Bot:")
prefix = input ("choisi le péfix:  ")
messagesend = input ("message a spam:  ")
print ("Le SPAM va commencer !")
prefix= prefix
    
client = commands.Bot(command_prefix=prefix)
    
@client.event
async def on_ready():
    print(Fore.GREEN + "Bot opérationelle ")
    await client.change_presence(activity=discord.Game(name="Bot create by Zerfox | my github: https://github.com/pommepoirechocolat"))
        
@client.command()
async def  nuke(ctx):
    guild = ctx.message.guild 
        
    n = 0
    while(n<=10):
        await ctx.channel.send(messagesend)
            
    while(n<=10):
        await ctx.channel.send(messagesend)
                
    while(n<=10):
        await ctx.channel.send(messagesend)
                
    while(n<=10):
        await ctx.channel.send(messagesend)
                
    while(n<=10):
        await ctx.channel.send(messagesend)


TOKEN = tokenraid
client.run(TOKEN)

