import unittest
import sys
import datetime

sys.path.append("..")

from spotify_api_wrapper.SpotifyAuthClient import SpotifyAuthClient
from spotify_api_wrapper.SpotifyApiException import SpotifyApiException

class TestSpotifyAuthClient(unittest.TestCase):
    def setUp(self):
        # Initialize a new instance of SpotifyAuthClient before each test
        self.auth_client = SpotifyAuthClient()

    def tearDown(self):
        # Reset the instance of SpotifyAuthClient after each test
        self.auth_client = None
    
    def test_authentication(self):    
        auth_client = SpotifyAuthClient()
        auth_client.authentication()

        self.assertEqual(len(auth_client.refresh_token), 131)
        self.assertTrue(isinstance(auth_client.refresh_token_expiry, datetime.datetime))
    
    def test_authentication_twice(self):
        auth_client = SpotifyAuthClient()
        auth_client.authentication()
        with self.assertRaises(SpotifyApiException):
            auth_client.authentication()

if __name__ == '__main__':
    unittest.main()
