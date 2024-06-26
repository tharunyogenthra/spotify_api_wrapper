from spotify_api_wrapper import SpotifyAPIWrapper

CLIENT_ID = "1830a9413e1d490f947ee1b6f14ee403"
REDIRECT_URL = "http://localhost:8888/callback"
USER_ID = '31qxnttkgyllhr4jassvn3pdzj6q'

sp = SpotifyAPIWrapper(client_id=CLIENT_ID, redirect_url=REDIRECT_URL)
sp.authentication(scope=['playlist-read-private', 'playlist-read-collaborative', 'user-top-read'])


top_tracks = sp.get_top_tracks(type="tracks", time_range="medium_term", limit=10, offset=0);
print(list(map(lambda x : x['name'], top_tracks['items'])))


playlists = sp.get_user_playlists(user_id="31qxnttkgyllhr4jassvn3pdzj6q", limit=50, offset=3)

for playlist in playlists.items:
    print(f'==>{playlist.name}<== ')

    tracks_url = playlist.tracks["href"]
    while tracks_url:
        tracks = sp.get_user_tracks(tracks_url)

        for track_item in tracks.items:
            print(f'\t{track_item.track.name}')

        tracks_url = tracks.next
    
