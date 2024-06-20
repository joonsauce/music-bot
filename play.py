from settings import *
from functions import *

@bot.command()
async def p(ctx, *, msg):
    await play_function(ctx, msg)

@bot.command()
async def play(ctx, *, msg):
    await play_function(ctx, msg)

async def play_function(ctx, msg):
    if await join_function(ctx, False) == -1:
        return
    info = get_info(msg)
    if info == -1:
        await ctx.send(errors)
        return
    player = ctx.message.guild.voice_client
    keys = list(info.keys())
    if 'url' in keys:
        await play_song(ctx, info, player)
    elif 'entries' in keys:
        await play_playlist(ctx, info, player)
    else:
        await ctx.send(errors)
