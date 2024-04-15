from spotify_api_wrapper import SpotifyAPIWrapper

CLIENT_ID = "1830a9413e1d490f947ee1b6f14ee403"
REDIRECT_URL = "http://localhost:8888/callback"
USER_ID = '31qxnttkgyllhr4jassvn3pdzj6q'

sp = SpotifyAPIWrapper(client_id=CLIENT_ID, redirect_url=REDIRECT_URL)
sp.authentication(scope=['playlist-read-private', 'playlist-read-collaborative'])

playlists = sp.get_user_playlists(user_id=USER_ID, limit=50, offset=3)

for i in range(0, len(playlists)):
    print(playlists.items[i].name)
