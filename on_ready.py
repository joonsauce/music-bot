with open ('secrets.txt', 'r') as secrets:
    bot_token = secrets.readline()
    master_server_id = secrets.readline()
    bot_owner_id = secrets.readline()
    spotify_id = secrets.readline()
    spotify_token = secrets.readline()
    youtube_key = secrets.readline()

ydl_opts = {
    'format': 'bestaudio/best',
    'noplaylist': 'True',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '128',
    }],
    'skip_download': 'True',
}

ffmpeg_opts = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn'
}

spotify_data = {
    'grant_type': 'client_credentials',
    'client_id': spotify_id,
    'client_secret': spotify_token
}