from discord.ext import commands
import os,traceback,discord,random,asyncio,time,sys
from discord.ext.commands import CommandNotFound
client = discord.Client()

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

#起動時に[○○をプレイ中]を表示させる
@bot.event
async def on_ready():
    guildco = str(len(bot.guilds))
    activname = "導入サーバー数" + guildco + " 現在開発モードです。"
    await bot.change_presence(activity=discord.Game(name=activname))
    before = time.monotonic()
    embed=discord.Embed(title="起動",description="編集中",color=discord.Color(random.randint(0,0xFFFFFF)))
    amsg = await asyncio.gather(*(c.send(embed=embed) for c in bot.get_all_channels() if c.name == 'ごりら起動ログ'))
    pong = (time.monotonic() - before) * 1000
    msg = "pong! : {0}ms \n 導入サーバー数 : {1}".format(pong,guildco)
    embed=discord.Embed(title="起動",description=msg,color=discord.Color(random.randint(0,0xFFFFFF)))
    await amsg.edit(embed=embed)

#━━ エラー ━━#
@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))

#存在しないコマンドが打たれた場合の処理
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        embed=discord.Embed(title="そのコマンドは存在しません！",color=discord.Color(random.randint(0,0xFFFFFF)))
        await ctx.send(embed=embed)
        return
    raise error

#━━━管理系━━━#    
@bot.command()
async def ping(ctx):
    before = time.monotonic()
    embed = discord.Embed(description="Pong!")
    msg = await ctx.send(embed=embed)
    ping = (time.monotonic() - before) * 1000
    embed = discord.Embed(description=f"Pong!\n`反応速度:`{int(ping)}ms")
    await msg.edit(embed=embed)
    
@bot.command()
async def restart(ctx):
    if ctx.author.id == 462557598231560193:
        embed=discord.Embed(title="強制再起動を開始します.",color=discord.Color(random.randint(0,0xFFFFFF)))
        await ctx.send(embed=embed)
        python = sys.executable
        os.execl(python, python, *sys.argv)
        
    else: embed=discord.Embed(title="このBOTの管理者以外は使用することができません。",color=discord.Color(random.randint(0,0xFFFFFF)))
    await ctx.send(embed=embed)
    
bot.run(token)
