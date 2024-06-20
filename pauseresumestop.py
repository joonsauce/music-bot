from settings import *

@bot.command()
async def skip(ctx, msg=''):
    loop_url[ctx.guild.id] = ''
    loop_title[ctx.guild.id] = ''
    if ctx.guild.id in players:
        if not msg:
            players[ctx.guild.id].stop()
            await ctx.send(skipping)
            return
        if not msg.isnumeric():
            await ctx.send(errors)
            return
        if int(msg) > len(titles[ctx.guild.id]):
            await ctx.send(errors)
        elif int(msg) == 1:
            await ctx.send(errors)
        else:
            for i in range(int(msg) - 1):
                links[ctx.guild.id].popleft()
                titles[ctx.guild.id].popleft()
            players[ctx.guild.id].stop()
            await ctx.send("Skipped `{}` song(s)!".format(msg))
    elif discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild).is_connected:
        await ctx.send(queue_empty)
    else:
        await ctx.send(bot_not_in_vc)

@bot.command()
async def pause(ctx):
    if ctx.guild.id in players:
        players[ctx.guild.id].pause()
        ctx.message.guild.voice_client.is_paused()
        await ctx.send(pausing)
    else:
        await ctx.send(bot_not_in_vc)

@bot.command()
async def resume(ctx):
    if ctx.guild.id in players:
        players[ctx.guild.id].resume()
        ctx.message.guild.voice_client.is_playing()
        await ctx.send(resuming)
    else:
        await ctx.send(bot_not_in_vc)
