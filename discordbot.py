from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def nyaa(ctx):
    await ctx.send('にゃーん')
    
    
"""メンバーのボイスチャンネル出入り時に実行されるイベントハンドラ"""
@.event
async def on_voice_state_update(member, before, after):
    



bot.run(token)
