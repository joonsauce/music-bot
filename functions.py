from joinleave import *
from settings import *
from spotify import *

def get_info(msg):
    try:
        get(msg)
    except:
        return yt_search(msg)
    else:
        check_spotify = check_spotify_link(msg)
        if check_spotify:
            check_playlist = check_spotify_playlist(msg)
            link = get_spotify_api_link(check_playlist, get_spotify_id(msg))
            if not check_playlist:
                title = get_track_info(link) + ' lyrics'
                return yt_search(title)
            else:
                playlist_info = get_playlist_info(link)
                return {'entries': [yt_search(title + ' lyrics') for title in playlist_info['songs']], 'title': playlist_info['title']}
        elif check_spotify == -1 or check_spotify == -2:
            print(check_spotify)
            return -1
        else:
            try:
                with YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(msg, download=False)
            except:
                return -1
            else:
                return info

def check_yt_playlist(url):
    return "/playlist?" in url

def yt_search(msg):
    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch:{msg}", download=False)['entries'][0]
    except:
        return -1
    else:
        return info

def next_song(id):
    now_playing[id] = ''
    if loop_url[id]:
        URL = loop_url[id]
        player = players[id]
        player.play(FFmpegPCMAudio(URL, **ffmpeg_opts), after=lambda x: next_song(id))
    elif links[id]:
        now_playing[id] = titles[id].popleft()
        now_url[id] = links[id].popleft()
        player = players[id]
        player.play(FFmpegPCMAudio(now_url[id], **ffmpeg_opts), after=lambda x: next_song(id))

async def play_song(ctx, info, player):
    URL = info['url']
    title = info['title']
    if player.is_playing() or player.is_paused():
        if ctx.guild.id in links:
            links[ctx.guild.id].append(URL)
            titles[ctx.guild.id].append(title)
        else:
            links[ctx.guild.id] = [URL]
            titles[ctx.guild.id] = [title]
        await ctx.send("Queued `{}`!".format(title))
    else:
        players[ctx.guild.id] = player
        links[ctx.guild.id] = deque()
        titles[ctx.guild.id] = deque()
        player.play(FFmpegPCMAudio(URL, **ffmpeg_opts), after=lambda x: next_song(ctx.guild.id))
        now_playing[ctx.guild.id] = title
        now_url[ctx.guild.id] = URL
        await ctx.send("Now playing: `{}`".format(title))

async def play_playlist(ctx, info, player):
    entries = info['entries']
    if player.is_playing() or player.is_paused():
        if ctx.guild.id in links:
            for item in entries:
                links[ctx.guild.id].append(item['url'])
                titles[ctx.guild.id].append(item['title'])
        else:
            links[ctx.guild.id] = [entries[0]['url']]
            titles[ctx.guild.id] = [entries[0]['title']]
            for item in range(1, len(entries)):
                links[ctx.guild.id].append(entries[item]['url'])
                titles[ctx.guild.id].append(entries[item]['title'])
        await ctx.send("Queued all from `{}`!".format(info['title']))
    else:
        players[ctx.guild.id] = player
        links[ctx.guild.id] = deque()
        titles[ctx.guild.id] = deque()
        player.play(FFmpegPCMAudio(entries[0]['url'], **ffmpeg_opts),
                    after=lambda x: next_song(ctx.guild.id))
        now_playing[ctx.guild.id] = entries[0]['title']
        now_url[ctx.guild.id] = entries[0]['url']
        await ctx.send("Now playing: `{}`".format(entries[0]['title']))
        for item in range(1, len(entries)):
            links[ctx.guild.id].append(entries[item]['url'])
            titles[ctx.guild.id].append(entries[item]['title'])
        await ctx.send("Queued the rest from `{}`!".format(info['title']))