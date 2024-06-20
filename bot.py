from convenience import *
from joinleave import *
from pauseresumestop import *
from play import *
from settings import *
from help import *

@bot.command()
async def announce(ctx, *, msg):
    if ctx.guild.id == master_server_id and ctx.message.author.id == bot_owner_id:
        servers = bot.guilds
        for server in servers:
            ss = bot.get_guild(server.id)
            channel = ss.system_channel
            if channel:
                await channel.send(msg)
            else:
                await ss.text_channels[0].send(msg)

bot.run(bot_token)
