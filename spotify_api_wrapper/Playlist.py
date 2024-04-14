import requests
from .SpotifyApiException import SpotifyApiException
import json
from .dataclasses.PlaylistDataClass import PlaylistDataClass

class Playlist:
    def __init__(self, auth_client):
        self.auth_client = auth_client
        
    def fetch_web_api(self, endpoint, method='GET', body=None):
        access_token = self.auth_client.access_token
        headers = {
            'Authorization': f'Bearer {access_token}'
        }
        response = requests.request(method, endpoint, headers=headers, json=body)
        response_status_code = response.status_code        

        if (response_status_code in [401, 403, 429]):
            response_content = response.content
            error_message = json.loads(response_content.decode('utf-8'))['error']['message']
            raise SpotifyApiException(f'ERROR {response.status_code} {error_message}')
        
        return response.json()
        
    def get_user_playlists(self, user_id, limit, offset):
        endpoint = f'https://api.spotify.com/v1/users/{user_id}/playlists?limit={limit}&offset={offset}'

        return PlaylistDataClass(self.fetch_web_api(endpoint))
        
