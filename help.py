from settings import *

@bot.command()
async def help(ctx, *, msg=''):
    embed = discord.Embed(color=None)
    embed.set_author(name="uwu do you need my help? >.<")
    if msg == '':
        # embed.add_field(name="auto", value='Makes the bot automatically queue songs after the current queue is over. '
        #                                    'To use this command, there must be at least 10 songs in the queue when the command is run. Usage: ~auto', inline=False)
        embed.add_field(name="dc", value='Makes the bot leave the voice channel it is in. Usage: ~dc', inline=False)
        embed.add_field(name="help", value="Displays the help menu. Usage: ~help", inline=False)
        embed.add_field(name="join", value='Makes bot join the voice channel the user is in. Usage: ~join', inline=False)
        embed.add_field(name="leave", value='Makes bot leave the voice channel it is in. Usage: ~leave', inline=False)
        embed.add_field(name="np", value='Makes bot display the currently playing song. Usage: ~np', inline=False)
        embed.add_field(name="p", value='Allows user to play a song they want. Usage: ~p <song title/link>', inline=False)
        embed.add_field(name="pause", value='Pauses the currently playing song. Usage: ~pause', inline=False)
        embed.add_field(name="q", value='Displays the currently queued song. Usage: ~q', inline=False)
        embed.add_field(name="queue", value='Displays the currently queued song. Usage: ~queue', inline=False)
        embed.add_field(name="remove",value='Makes the bot remove a song from the queue. Usage: ~remove <song number from ~q command>',inline=False)
        embed.add_field(name="resume", value='Resumes currently paused song. Usage: ~resume', inline=False)
        embed.add_field(name="rmv",value='Makes the bot remove a song from the queue. Usage: ~shuffle',inline=False)
        embed.add_field(name="shuffle",value='Makes the bot shuffle songs in the queue. Usage: ~rmv <song number from ~q command>',inline=False)
        embed.add_field(name="skip", value='Makes bot skip whatever music is playing. Usage: ~skip <number of songs wanting to skip>', inline=False)
        embed.add_field(name="song", value='Makes bot display the currently playing song. Usage: ~song', inline=False)
    # elif msg == 'auto':
    #     embed.add_field(name="auto", value='Makes the bot automatically queue songs after the current queue is over. '
    #                                        'To use this command, there must be at least 10 songs in the queue when the command is run. Usage: ~auto', inline=False)
    elif msg == 'dc':
        embed.add_field(name="dc", value='Makes the bot leave the voice channel it is in. Usage: ~dc', inline=False)
    elif msg == 'help':
        embed.add_field(name="help", value="Displays the help menu. Usage: ~help", inline=False)
    elif msg == 'join':
        embed.add_field(name="join", value='Makes bot join the voice channel the user is in. Usage: ~join', inline=False)
    elif msg == 'leave':
        embed.add_field(name="leave", value='Makes bot leave the voice channel it is in. Usage: ~leave', inline=False)
    elif msg == 'np':
        embed.add_field(name="np", value='Makes bot display the currently playing song. Usage: `np', inline=False)
    elif msg == 'p' or msg == 'play':
        embed.add_field(name="p", value='Allows user to play a song they want. Usage: ~p <song title/link>', inline=False)
    elif msg == 'pause':
        embed.add_field(name="pause", value='Pauses the currently playing song. Usage: ~pause', inline=False)
    elif msg == 'q' or msg == 'queue':
        embed.add_field(name="q", value='Displays the currently queued song. Usage: ~q', inline=False)
    elif msg == 'resume':
        embed.add_field(name="resume", value='Resumes currently paused song. Usage: ~resume', inline=False)
    elif msg == 'rmv' or msg == 'remove':
        embed.add_field(name="rmv",value='Makes the bot remove a song from the queue. Usage: ~rmv <song number from ~q command>',inline=False)
    elif msg =='shuffle':
        embed.add_field(name="shuffle", value='Makes the bot shuffle songs in the queue. Usage: ~rmv <song number from ~q command>', inline=False)
    elif msg == 'skip':
        embed.add_field(name="skip",value='Makes bot skip whatever music is playing. Usage: ~skip <number of songs wanting to skip>',inline=False)
    elif msg == 'song':
        embed.add_field(name="song", value='Makes bot display the currently playing song. Usage: ~song', inline=False)
    else:
        embed.add_field(name="No command", value='There is no command with that name. Use ~help to view the full list of commands', inline=False)
    await ctx.send(embed=embed)
