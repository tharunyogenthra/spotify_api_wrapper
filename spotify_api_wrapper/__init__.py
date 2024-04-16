from .SpotifyAuthClient import SpotifyAuthClient
from .SpotifyAPIClient import SpotifyAPIClient

class SpotifyAPIWrapper:
    def __init__(self, client_id, redirect_url):
        """
        Initializes the SpotifyAPIWrapper by creating instances of the SpotifyAuthClient and SpotifyAPIClient.
        """
        self.auth_client = SpotifyAuthClient(client_id, redirect_url)
        self.api_client = SpotifyAPIClient(self.auth_client)

    def authentication(self, scope):
        """
        Performs the Spotify authentication flow and retrieves the necessary access tokens. Raises error if already authenticated

        Args:
            scope (str, optional): The scope of permissions to request from the user. Defaults to 'user-library-read'.
        """
        self.auth_client.authentication(scope)

    def refresh_access_token(self):
        """
        Refreshes the access token using the stored refresh token. Raises error if token is not expired yet
        """
        self.auth_client.refresh_access_token()

    def get_user_playlists(self, user_id, limit=50, offset=0):
        """
        Retrieves the user's playlists in a PlaylistDataClass.

        Returns:
            PlaylistDataClass object containing many SimplifiedPlaylistObject
        """
        return self.api_client.get_user_playlists(user_id, limit, offset)
    
    def get_user_tracks(self, url, limit=50, offset=0):
        """
        Retrieves the list of the user tracks with a specifed url i.e https://api.spotify.com/v1/playlists/47zRuvzZdm5MojFoL4rkBy/tracks

        Args:
            url (string): url of the tracks
        """
        return self.api_client.get_user_tracks(url, limit, offset)

    def search_tracks(self, query):
        """
        Searches for tracks on Spotify based on the provided query.

        Args:
            query (str): The search query, e.g., "artist:Radiohead".

        Returns:
            dict: The search results.
        """
        return self.api_client.search_tracks(query)