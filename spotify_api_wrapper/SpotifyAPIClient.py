from .Playlist import Playlist
from .Track import Track

class SpotifyAPIClient:
    def __init__(self, auth_client):
        self.auth_client = auth_client
        self.play_list = Playlist(self.auth_client)
        self.track = Track(self.auth_client)

    def get_user_playlists(self, user_id, limit, offset):
        return self.play_list.get_user_playlists(user_id, limit, offset)
    
    def get_user_tracks(self, url, limit, offset):
        return self.track.get_user_tracks(url, limit, offset)

    def search_tracks(self, query):
        print("search_tracks " + query)