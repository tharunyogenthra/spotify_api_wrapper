from spotify_api_wrapper import SpotifyAPIWrapper

sp = SpotifyAPIWrapper()
sp.authentication()
sp.authentication()

playlists = sp.get_user_playlists()
search_results = sp.search_tracks("artist:Radiohead")