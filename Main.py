# Importing
import discord,requests,os,threading, time
from time import sleep
from discord.ext import commands

# Define discord stuff
token = "Bot Token Here"
client = discord.Client()
client = commands.Bot (command_prefix='!')
client.remove_command('help')

# Print client detials on startup
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

# Making a function to thread that requests to the site
def SPAM(code,option,proxy):
    requests.post(f"https://www.strawpoll.me/{code}",data={"options": option}, proxies={'https': f'http://{proxy}'}, timeout=10)

# Making the help command
@client.command()
async def help(ctx):
    embed = discord.Embed(title='Shard Help', description=f'''```asciidoc
Spam               :: [Code] [Option]
```''', color=0x2f3136,icon_url=ctx.author.avatar_url , timestamp=ctx.message.created_at)
    await ctx.send(embed=embed)

# Making the spam command 
@client.command()
async def spam(ctx, code, option):
    About = 0
    proxies = requests.get('https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=1000&country=all&ssl=all&anonymity=all').text
    for a in proxies.splitlines():
        About += 1
        threading.Thread(target=SPAM, args=(code,option,a,)).start()
    Sending = discord.Embed(title='Starting Spam', color=0x2f3136,icon_url=ctx.author.avatar_url , timestamp=ctx.message.created_at)
    msg = await ctx.send(embed=Sending)
    embed = discord.Embed(title='Finished Spamming', description=f'''```asciidoc
Sent About     :: [{About}]
```''', color=0x2f3136,icon_url=ctx.author.avatar_url , timestamp=ctx.message.created_at)
    time.sleep(10)
    await msg.edit(embed=embed)

# Runing the bot
client.run(token)
