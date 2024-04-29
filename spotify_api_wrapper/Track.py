import requests
from .SpotifyApiException import SpotifyApiException
import json
from .dataclasses.TrackDataClass import TrackDataClass

class Track:
    def __init__(self, auth_client):
        self.auth_client = auth_client
        
    def fetch_web_api(self, endpoint, method='GET', body=None):
        access_token = self.auth_client.access_token
        headers = {
            'Authorization': f'Bearer {access_token}'
        }
        response = requests.request(method, endpoint, headers=headers, json=body)
        response_status_code = response.status_code        

        if (response_status_code in [400, 401, 403, 404, 429]):
            response_content = response.content
            error_message = json.loads(response_content.decode('utf-8'))['error']['message']
            raise SpotifyApiException(f'ERROR {response.status_code} {error_message}')
        
        return response.json()
        
    def get_user_tracks(self, url, limit, offset):
        # 'https://api.spotify.com/v1/playlists/3cEYpjA9oz9GiPac4AsH4n/tracks?limit=10&offset=0'
        if ("limit" in url):
            endpoint = f'{url}'
        else:
            endpoint = f'{url}?limit={limit}&offset={offset}'

        return TrackDataClass(self.fetch_web_api(endpoint))
        
    def get_top_tracks(self, type, time_range, limit, offset):
        # 'https://api.spotify.com/v1/me/top/artists?time_range=HELLO&limit=HELLO&offset=HELLO'
        endpoint = f'https://api.spotify.com/v1/me/top/{type}?time_range={time_range}&limit={limit}&offset={offset}'
        return self.fetch_web_api(endpoint=endpoint)