from settings import *

def check_spotify_link(link):
    try:
        response = get(link)
    except:
        return -1
    else:
        if response.status_code != 200:
            return -2
        if 'spotify' in link.split('.'):
            return True

def check_spotify_playlist(link):
    split_link = link.split('/')
    if 'playlist' in split_link:
        return True
    elif 'track' in split_link:
        return False
    else:
        return -1

def get_spotify_id(link):
    return link.split('/')[-1]

def get_spotify_token():
    response = requests.post('https://accounts.spotify.com/api/token', data=spotify_data)

    if response.status_code != 200:
        return -1
    return response.json()['access_token']

def get_spotify_api_link(playlist, id):
    if playlist:
        return 'https://api.spotify.com/v1/playlists/' + id
    else:
        return 'https://api.spotify.com/v1/tracks/' + id