import discord, os, requests, json, colorama

from colorama import Fore, Style
colorama.init()

from discord.ext import commands


with open('config.json') as f:
    config = json.load(f)

token = config.get('token')
prefix = config.get('prefix')

bot = commands.Bot(description='Selfbot', command_prefix=prefix, self_bot=True)
bot.remove_command('help')

@bot.event
async def on_connect():
    print(f'''{Style.DIM}
{Fore.RED}
         ██████╗██╗   ██╗████████╗███████╗██████╗  ██████╗ ████████╗
        ██╔════╝██║   ██║╚══██╔══╝██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝
        ██║     ██║   ██║   ██║   █████╗  ██████╔╝██║   ██║   ██║   
        ██║     ██║   ██║   ██║   ██╔══╝  ██╔══██╗██║   ██║   ██║   
        ╚██████╗╚██████╔╝   ██║   ███████╗██████╔╝╚██████╔╝   ██║   
         ╚═════╝ ╚═════╝    ╚═╝   ╚══════╝╚═════╝  ╚═════╝    ╚═╝                        
{Fore.RESET}    {Style.RESET_ALL}
    {Fore.RED}User:{Fore.RESET} {bot.user.name}
    {Fore.RED}Prefix:{Fore.RESET} {prefix}
    {Fore.RED}Connected and Ready for use!{Fore.RESET}''')

@bot.event
async def on_message_edit(before, after):
    await bot.process_commands(after)

@bot.command()
async def slap(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/slap")
    res = r.json()
    embed = discord.Embed(description=f"**{ctx.author.mention} Slaps {user.mention}**")
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)

@bot.command()
async def slapdm(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/slap")
    res = r.json()
    embed = discord.Embed(description=f"*get slapped*")
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)

@bot.command()
async def hug(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/hug")
    res = r.json()
    embed = discord.Embed(description=f"**{ctx.author.mention} Hugs {user.mention}**")
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)

@bot.command()
async def hugdm(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/hug")
    res = r.json()
    embed = discord.Embed(description=f"*get hugged*")
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)

@bot.command()
async def kiss(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/kiss")
    res = r.json()
    embed = discord.Embed(description=f"**{ctx.author.mention} Kisses {user.mention}**")
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)

@bot.command()
async def kissdm(ctx):
    await ctx.mssage.delete()
    r = requests.get("https://nekos.life/api/v2/img/kiss")
    res = r.json()
    embed = discord.Embed(description=f"*get kissed*")
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)

@bot.command()
async def pat(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/pat")
    res = r.json()
    embed = discord.Embed(description=f"**{ctx.author.mention} pats {user.mention}**")
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)

@bot.command()
async def patdm(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/pat")
    res = r.json()
    embed = discord.Embed(description=f"*pats you*")
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)


@bot.command()
async def cuddle(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/cuddle")
    res = r.json()
    embed = discord.Embed(description=f"**{ctx.author.mention} cuddles {user.mention}**")
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)

@bot.command()
async def cuddledm(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/cuddle")
    res = r.json()
    embed = discord.Embed(description=f"*cuddles with you*")
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)

@bot.command()
async def help(ctx):
    await ctx.message.delete()
    await ctx.send(f'''**General:**\n*{prefix}kiss [@user]:* Kisses the mentioned user.\n*{prefix}hug [@user]:* Hugs the mentioned user. \n*{prefix}slap [@user]:* Slaps the mentioned user. \n*{prefix}pat [@user]:* Pats a mentioned user. \n*{prefix}cuddle [@user]:* Cuddles the mentioned user. \n*{prefix}kissdm:* Kisses the user.\n*{prefix}hugdm:* Hugs the user. \n*{prefix}slapdm:* Slaps the user. \n*{prefix}patdm:* Pats a user. \n*{prefix}cuddledm:* Cuddles the user.''')

bot.run(token, bot=False)