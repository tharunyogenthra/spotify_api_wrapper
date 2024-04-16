import base64
import hashlib
import os
import requests
from urllib.parse import urlencode
import webbrowser
from datetime import datetime, timedelta
from .SpotifyApiException import SpotifyApiException
import json

with open('spotify_api_wrapper/config.json', 'r') as f:
    config = json.load(f)
    
class SpotifyAuthClient:
    """
    Handles Spotify authentication and token management.

    Attributes:
        client_id (str): The Spotify client ID.
        redirect_uri (str): The redirect URI for the Spotify application.
        refresh_token (str): The refresh token for the Spotify user.
        refresh_token_expiry (datetime): The expiration time of the refresh token.
    """

    def __init__(self, client_id, redirect_uri):
        """
        Initializes the SpotifyAuthClient with the provided client ID and redirect URI.

        Args:
            client_id (str, optional): The Spotify client ID. Defaults to the value from the config module.
            redirect_uri (str, optional): The redirect URI for the Spotify application. Defaults to the value from the config module.
        """
        self.client_id = client_id
        self.redirect_uri = redirect_uri
        self.refresh_token = None
        self.refresh_token_expiry = None
        self.access_token = None
        
        config["SPOTIFY_CLIENT_ID"] = client_id
        config["SPOTIFY_REDIRECT_URI"] = redirect_uri
        
        with open('spotify_api_wrapper/config.json', 'w') as f:
            json.dump(config, f)

    def check_if_refresh_expired(self):
        """
        Checks if the refresh token has expired.

        Returns:
            bool: True if the refresh token has expired, False otherwise.
        """
        return datetime.now() >= self.refresh_token_expiry

    @property
    def get_refresh_token(self):
        """
        Returns the refresh token.

        Returns:
            str: The refresh token.
        """
        return self.refresh_token

    @property
    def get_refresh_token_expiry(self):
        """
        Returns the expiration time of the refresh token.

        Returns:
            datetime: The expiration time of the refresh token.
        """
        return self.refresh_token_expiry
    
    @property
    def get_access_token(self):
        """
        Returns the expiration time of the refresh token.

        Returns:
            datetime: The expiration time of the refresh token.
        """
        return self.access_token

    def generate_random_string(self, length=32):
        """
        Generates a random string of the specified length.

        Args:
            length (int, optional): The length of the random string. Defaults to 32.

        Returns:
            str: A random string of the specified length.
        """
        return os.urandom(length).hex()

    def generate_pkce(self):
        """
        Generates a PKCE code verifier and challenge.

        PKCE (Proof Key for Code Exchange) is a security enhancement to the OAuth 2.0 authorization
        flow. The code verifier is a random, high-entropy string, and the code challenge is a
        SHA-256 hash of the code verifier, converted to a URL-safe base64 string.

        Returns:
            tuple: A tuple containing the code verifier and code challenge.
        """
        code_verifier = self.generate_random_string()
        code_challenge = base64.urlsafe_b64encode(hashlib.sha256(code_verifier.encode()).digest()).decode().rstrip('=')
        return code_verifier, code_challenge

    def authentication(self, scope):
        """
        Performs the Spotify authentication flow and retrieves the refresh token.

        Args:
            scope (str, optional): The scope of permissions to request from the user. Defaults to 'user-library-read'.
        """

        if (config["REFRESH_TOKEN_EXPIRY"] != ''):
            self.refresh_token_expiry = datetime.strptime(config["REFRESH_TOKEN_EXPIRY"], '%Y-%m-%dT%H:%M:%S.%f')
            if (self.check_if_refresh_expired() == True):
                self.refresh_access_token_func()
            
            self.client_id = config["SPOTIFY_CLIENT_ID"]
            self.redirect_uri = config["SPOTIFY_REDIRECT_URI"]
            self.refresh_token = config["REFRESH_TOKEN"]
            self.access_token = config["ACCESS_TOKEN"]
            
            print("\nAuthentication is successful!!\n")
            return;
            
                
        # Generate the PKCE code verifier and challenge
        code_verifier, code_challenge = self.generate_pkce()

        # Build the authorization URL with the necessary parameters
        auth_url = 'https://accounts.spotify.com/authorize'
        auth_params = {
            'client_id': self.client_id,
            'response_type': 'code',
            'redirect_uri': self.redirect_uri,
            'code_challenge_method': 'S256',
            'code_challenge': code_challenge,
            'scope': (" ").join(scope)
        }
        auth_url_with_params = auth_url + '?' + urlencode(auth_params)
        # print(auth_url_with_params)
        webbrowser.open(auth_url_with_params)

        # Get the authorization code from the redirected URL
        redirected_url = input("Enter the redirected URL after authorisation is complete: ")
        code = redirected_url.split('?code=')[1].split('&')[0]

        # Exchange the authorization code for an access token and refresh token
        token_url = 'https://accounts.spotify.com/api/token'
        token_params = {
            'client_id': self.client_id,
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': self.redirect_uri,
            'code_verifier': code_verifier
        }
        token_response = requests.post(token_url, data=token_params)
        token_info = token_response.json()
        
        # print(token_response, token_info)
        self.access_token = token_info.get('access_token')
        self.refresh_token = token_info.get('refresh_token')
        if 'expires_in' in token_info:
            expires_in = token_info['expires_in']
            self.refresh_token_expiry = datetime.now() + timedelta(seconds=expires_in)
            
        config["REFRESH_TOKEN"] = self.refresh_token
        config["REFRESH_TOKEN_EXPIRY"] = self.refresh_token_expiry.isoformat()
        config["ACCESS_TOKEN"] = self.access_token
        
        with open('spotify_api_wrapper/config.json', 'w') as f:
            json.dump(config, f)

        print("\nAuthentication is successful!!\n")

    def refresh_access_token_func(self):
        """
        Refreshes the access token using the stored refresh token.
        """
        token_url = 'https://accounts.spotify.com/api/token'
        token_params = {
            'client_id': self.client_id,
            'grant_type': 'refresh_token',
            'refresh_token': config["REFRESH_TOKEN"]
        }
        token_response = requests.post(token_url, data=token_params)
        token_info = token_response.json()
        self.refresh_token = token_info.get('refresh_token', self.refresh_token)
        self.access_token = token_info.get('access_token')
        self.refresh_token = token_info.get('refresh_token')
        
        if 'expires_in' in token_info:
            expires_in = token_info['expires_in']
            # print(f'==>{datetime.now() + timedelta(seconds=expires_in)}<==')
            self.refresh_token_expiry = datetime.now() + timedelta(seconds=expires_in)
            
        config["REFRESH_TOKEN"] = self.refresh_token
        config["REFRESH_TOKEN_EXPIRY"] = self.refresh_token_expiry.isoformat()
        config["ACCESS_TOKEN"] = self.access_token
        
        with open('spotify_api_wrapper/config.json', 'w') as f:
            json.dump(config, f)
            
        