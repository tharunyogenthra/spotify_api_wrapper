import unittest
import datetime
import json

from spotify_api_wrapper import SpotifyAPIWrapper
from spotify_api_wrapper.SpotifyApiException import SpotifyApiException
from spotify_api_wrapper.dataclasses.PlaylistDataClass import PlaylistDataClass 

with open('config_test.json', 'r') as f:
    config = json.load(f)

class Tests(unittest.TestCase):
    '''
    test SpotifyAuthClient
    '''
    def test_authentication(self):    
        sp = SpotifyAPIWrapper(config["SPOTIFY_CLIENT_ID"], config["SPOTIFY_REDIRECT_URI"])
        sp.authentication(scope=['playlist-read-private', 'playlist-read-collaborative'])

        self.assertEqual(len(sp.auth_client.refresh_token), 134)
        self.assertTrue(isinstance(sp.auth_client.refresh_token_expiry, datetime.datetime))
        
    def test_authentication_refresh_token_length(self):    
        sp = SpotifyAPIWrapper(config["SPOTIFY_CLIENT_ID"], config["SPOTIFY_REDIRECT_URI"])
        sp.authentication(scope=['playlist-read-private', 'playlist-read-collaborative'])

        self.assertEqual(len(sp.auth_client.refresh_token), 134)
        self.assertTrue(isinstance(sp.auth_client.refresh_token_expiry, datetime.datetime))
        
    '''
    test Playlist
    '''
    
    def test_playlist_invalid_user_id(self):
        sp = SpotifyAPIWrapper(config["SPOTIFY_CLIENT_ID"], config["SPOTIFY_REDIRECT_URI"])
        sp.authentication(scope=['playlist-read-private', 'playlist-read-collaborative'])
        
        self.assertRaises(SpotifyApiException, lambda: sp.get_user_playlists(user_id="IAMWRONG", limit=50, offset=3))
        
    def test_playlist_invalid_limit_above_50(self):
        sp = SpotifyAPIWrapper(config["SPOTIFY_CLIENT_ID"], config["SPOTIFY_REDIRECT_URI"])
        sp.authentication(scope=['playlist-read-private', 'playlist-read-collaborative'])
        
        self.assertRaises(SpotifyApiException, lambda: sp.get_user_playlists(user_id="31qxnttkgyllhr4jassvn3pdzj6q", limit=51, offset=3))
        
    def test_playlist_invalid_above_100(self):
        sp = SpotifyAPIWrapper(config["SPOTIFY_CLIENT_ID"], config["SPOTIFY_REDIRECT_URI"])
        sp.authentication(scope=['playlist-read-private', 'playlist-read-collaborative'])
        
        self.assertRaises(SpotifyApiException, lambda: sp.get_user_playlists(user_id="31qxnttkgyllhr4jassvn3pdzj6q", limit=-50, offset=100))
        
    def test_playlist_return_correct(self):
        sp = SpotifyAPIWrapper(config["SPOTIFY_CLIENT_ID"], config["SPOTIFY_REDIRECT_URI"])
        sp.authentication(scope=['playlist-read-private', 'playlist-read-collaborative'])
        
        playlist = sp.get_user_playlists(user_id="31qxnttkgyllhr4jassvn3pdzj6q", limit=50)
        self.assertTrue(type(playlist), PlaylistDataClass)
        self.assertGreater(len(playlist), 10)
        
        
        
if __name__ == '__main__':
    unittest.main()

