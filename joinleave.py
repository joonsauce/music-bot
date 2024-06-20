from settings import *

@bot.command()
async def join(ctx):
    await join_function(ctx, True)

@bot.command()
async def leave(ctx):
    await leave_function(ctx)

@bot.command()
async def dc(ctx):
    await leave_function(ctx)

@bot.command()
async def disconnect(ctx):
    await leave_function(ctx)

async def join_function(ctx, join_tag: bool):
    voice = ctx.author.voice
    if not voice:
        await ctx.send(need_connect)
        return -1
    if not voice.channel:
        await ctx.send(need_connect)
        return -1
    if ctx.message.guild.voice_client:
        if join_tag:
            await ctx.send(already_connected)
        return
    await voice.channel.connect()
    links[ctx.message.guild.id] = deque()
    titles[ctx.message.guild.id] = deque()
    loop_url[ctx.message.guild.id] = ''
    loop_title[ctx.message.guild.id] = ''
    await ctx.send("Connected to `{}`!".format(voice.channel))

async def leave_function(ctx):
    channel = ctx.message.guild.voice_client
    if channel:
        links[ctx.message.guild.id] = deque()
        titles[ctx.message.guild.id] = deque()
        loop_url[ctx.message.guild.id] = ''
        loop_title[ctx.message.guild.id] = ''
        await channel.disconnect()
        await ctx.send(disconnected)
    else:
        await ctx.send(bot_not_in_vc)