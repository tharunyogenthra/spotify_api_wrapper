from .SpotifyAuthClient import SpotifyAuthClient
from .SpotifyAPIClient import SpotifyAPIClient

class SpotifyAPIWrapper:
    """
    Provides a convenient wrapper around the Spotify API, handling authentication and API interactions.

    Attributes:
        auth_client (SpotifyAuthClient): The authentication client responsible for managing Spotify authorization.
        api_client (SpotifyAPIClient): The API client used to make requests to the Spotify API.
    """

    def __init__(self):
        """
        Initializes the SpotifyAPIWrapper by creating instances of the SpotifyAuthClient and SpotifyAPIClient.
        """
        self.auth_client = SpotifyAuthClient()
        self.api_client = SpotifyAPIClient(self.auth_client)

    def authentication(self, scope='user-library-read'):
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

    def get_user_playlists(self):
        """
        Retrieves the user's playlists.

        Returns:
            list: A list of the user's playlists.
        """
        return self.api_client.get_user_playlists()

    def search_tracks(self, query):
        """
        Searches for tracks on Spotify based on the provided query.

        Args:
            query (str): The search query, e.g., "artist:Radiohead".

        Returns:
            dict: The search results.
        """
        return self.api_client.search_tracks(query)