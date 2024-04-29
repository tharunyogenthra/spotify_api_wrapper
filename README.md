# Spotify API Wrapper

The Spotify API Wrapper is a Python package that simplifies the interaction with the Spotify Web API. It provides a convenient interface to authenticate with the Spotify API, retrieve user playlists, tracks, search for tracks, and more.

## Features

- Authenticate with the Spotify API using the Client Credentials Flow
- Retrieve user playlists
- Retrieve tracks from user playlists
- Search for tracks on Spotify
- Get the user's top tracks for a specific time range
- Refresh access tokens automatically

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/spotify-api-wrapper.git
    ```

2. Navigate to the project directory:

    ```bash
    cd spotify-api-wrapper
    ```

3. Create a virtual environment (recommended):

    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

- Import the `SpotifyAPIWrapper` class from the package:

    ```python
    from spotify_api_wrapper import SpotifyAPIWrapper
    ```

- Create an instance of `SpotifyAPIWrapper` with your Spotify client ID and redirect URI:

    ```python
    client_id = 'your_spotify_client_id'
    redirect_uri = 'your_spotify_redirect_uri'
    spotify_wrapper = SpotifyAPIWrapper(client_id, redirect_uri)
    ```

- Authenticate with the Spotify API:

    ```python
    spotify_wrapper.authentication(scope=['user-library-read'])
    ```

- Use the available methods to interact with the Spotify API:

    ```python
    # Get the user's playlists
    user_playlists = spotify_wrapper.get_user_playlists('user_id')

    # Get the user's tracks from a playlist
    playlist_tracks = spotify_wrapper.get_user_tracks('https://api.spotify.com/v1/playlists/playlist_id/tracks')

    # Search for tracks
    search_results = spotify_wrapper.search_tracks('query')

    # Get the user's top tracks
    top_tracks = spotify_wrapper.get_top_tracks('tracks', time_range='medium_term', limit=50, offset=0)
    ```

## Contributing

Contributions to the Spotify API Wrapper are welcome! If you find any issues or want to add new features, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
