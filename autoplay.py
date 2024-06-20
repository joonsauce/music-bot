from spotify_api import *

'''
format of the autoplay function
- if msg == 'q' or 'queue', then use songs in queue to add some songs to end of queue
    - this should only work if there are more than 10 songs in queue
- else, use comma delimited form for songs and length should be longer than 10
'''

def check_autoplay_message(msg):
    if msg == 'q' or msg =='queue':
        return False
    return True

def get_autoplay_spotify_ids(songs):
    headers = {
        'Authorization': 'Bearer  {}'.format(get_spotify_token())
    }
    for song in songs:
        response = get(get_spotify_search_url(song), headers=headers)

def get_spotify_search_url(query):
    return 'https://api.spotify.com/v1/search?q=' + query + '&type=track'

@bot.command()
async def autoplay(ctx, *, msg):
    if check_autoplay_message(msg):
        songs = msg.split(',')
    else:
        songs = titles[ctx.guild.id]
    # update to be 10 before release
    if len(songs) < 1:
        await ctx.send("There must be more than 10 songs to use autoplay. Please queue more songs or "
                       "include more songs in list")
    else:
        get_autoplay_spotify_ids(songs)