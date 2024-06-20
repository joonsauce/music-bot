from settings import *

@bot.command()
async def q(ctx):
    await queue_function(ctx)

@bot.command()
async def queue(ctx):
    await queue_function(ctx)

async def queue_function(ctx):
    embed = discord.Embed(color=None)
    embed.set_author(name="{}'s queue".format(ctx.guild))
    if ctx.guild.id in now_playing:
        if not now_playing[ctx.guild.id]:
            embed.add_field(name=errors, value=queue_empty, inline=False)
        else:
            embed.add_field(name="Currently playing:", value="{}".format(now_playing[ctx.guild.id]), inline=False)
            for num in range(len(titles[ctx.guild.id])):
                embed.add_field(name=str(num + 1), value="{}".format(titles[ctx.guild.id][num]), inline=False)
    else:
        embed.add_field(name=errors, value=queue_empty, inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def np(ctx):
    await np_function(ctx)

@bot.command()
async def song(ctx):
    await np_function(ctx)

async def np_function(ctx):
    if ctx.guild.id in now_playing:
        if now_playing[ctx.guild.id]:
            await ctx.send("Currently playing: `{}`".format(now_playing[ctx.guild.id]))
        else:
            await ctx.send(no_play)
    else:
        await ctx.send(no_play)

@bot.command()
async def remove(ctx, msg):
    if not ctx.guild.id in titles:
        await ctx.send(no_play)
    if not str(msg).isnumeric():
        await ctx.send("Please input a positive integer (whole number) corresponding to a song on the queue.")
        return
    if not float(msg).is_integer():
        await ctx.send("Please input a positive integer (whole number) corresponding to a song on the queue.")
        return
    if int(msg) < 1:
        await ctx.send("Please input a positive integer (whole number) corresponding to a song on the queue.")
        return

    numOfSongs = len(titles[ctx.guild.id])

    if not numOfSongs >= int(msg):
        await ctx.send("Please input a positive integer (whole number) corresponding to a song on the queue.")
        return

    title = titles[ctx.guild.id][int(msg) - 1]
    titles[ctx.guild.id].pop(int(msg) - 1)
    links[ctx.guild.id].pop(int(msg) - 1)
    await ctx.send("Removed `{}` from queue!".format(title))

@bot.command()
async def rmv(ctx, msg):
    if not ctx.guild.id in titles:
        await ctx.send(no_play)
    if not str(msg).isnumeric():
        await ctx.send("Please input a positive integer (whole number) corresponding to a song on the queue.")
        return
    if not float(msg).is_integer():
        await ctx.send("Please input a positive integer (whole number) corresponding to a song on the queue.")
        return
    if int(msg) < 1:
        await ctx.send("Please input a positive integer (whole number) corresponding to a song on the queue.")
        return

    numOfSongs = len(titles[ctx.guild.id])

    if not numOfSongs >= int(msg):
        await ctx.send("Please input a positive integer (whole number) corresponding to a song on the queue.")
        return

    title = titles[ctx.guild.id][int(msg) - 1]
    del titles[ctx.guild.id][int(msg) - 1]
    del links[ctx.guild.id][int(msg) - 1]
    await ctx.send("Removed `{}` from queue!".format(title))

@bot.command()
async def loop(ctx):
    if ctx.guild.id not in now_playing:
        await ctx.send(no_play)
        return
    loop_title[ctx.guild.id] = now_playing[ctx.guild.id]
    loop_url[ctx.guild.id] = now_url[ctx.guild.id]
    await ctx.send("Looped `{}`!".format(now_playing[ctx.guild.id]))

@bot.command()
async def shuffle(ctx):
    if not ctx.message.guild.voice_client:
        await ctx.send(need_connect)
        return
    guild_id = ctx.guild.id
    if not titles[guild_id]:
        await ctx.send(queue_empty)
        return
    title_list = titles[guild_id]
    link_list = titles[guild_id]
    # associate link with title and associate it with uuid for shuffling
    joined_dict = dict()
    for i in range(len(title_list)):
        internal_values = (title_list.popleft(), link_list.popleft())
        joined_dict[uuid.uuid4()] = internal_values
    key_list = list(joined_dict.keys())
    random.shuffle(key_list)
    new_titles_list = deque()
    new_links_list = deque()
    for key in key_list:
        new_titles_list.append(joined_dict[key][0])
        new_links_list.append(joined_dict[key][1])
    titles[guild_id] = new_titles_list
    links[guild_id] = new_links_list
    await ctx.send("Shuffled the queue!")
