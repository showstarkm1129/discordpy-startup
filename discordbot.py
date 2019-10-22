from discord.ext import commands
import os,traceback,discord,random,asyncio,time
from discord.ext.commands import CommandNotFound
client = discord.Client()

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
#━━ エラー ━━#
#ゴリラ
@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))

#存在しないコマンドが打たれた場合の処理
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        embed=discord.Embed(title="そのコマンドは存在しません！",color=discord.Color(random.randint(0,0xFFFFFF)))
        await ctx.send(embed=embed)

@bot.command()
async def ping(ctx):
    before = time.monotonic()
    embed = discord.Embed(description="Pong!")
    msg = await ctx.send(embed=embed)
    ping = (time.monotonic() - before) * 1000
    embed = discord.Embed(description=f"Pong!\n`反応速度:`{int(ping)}ms")
    await msg.edit(embed=embed)

bot.run(token)
