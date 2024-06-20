from spotify_api import *

def get_track_info(link):
    headers = {
        'Authorization': 'Bearer  {}'.format(get_spotify_token())
    }

    response = get(link, headers=headers)

    if response.status_code != 200:
        return -1
    info = response.json()

    if len(info['artists']) > 1:
        artist_list = [j['name'] for j in info['artists']]
        artist = ', '.join(artist_list)
    else:
        artist = info['artists'][0]['name']

    return artist + ' - ' + info['name']

def get_playlist_info(link):
    headers = {
        'Authorization': 'Bearer  {}'.format(get_spotify_token())
    }

    response = get(link, headers=headers)

    if response.status_code != 200:
        return -1
    info = response.json()

    simpl = info['tracks']['items']

    playlist_information = {}

    song_information = deque()

    for i in simpl:
        track = i['track']

        if len(track['artists']) > 1:
            artist_list = [j['name'] for j in track['artists']]
            artist = ', '.join(artist_list)
        else:
            artist = track['artists'][0]['name']
        song_information.append(artist + ' - ' + track['name'])

    playlist_information['songs'] = song_information
    playlist_information['title'] = info['name']

    return playlist_information

