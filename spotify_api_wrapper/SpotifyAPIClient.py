class SpotifyAPIClient:
    def __init__(self, auth_client):
        self.auth_client = auth_client

    def get_user_playlists(self):
        print("get_user_playlists")

    def search_tracks(self, query):
        print("search_tracks " + query)