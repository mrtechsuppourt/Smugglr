import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Set your Spotify API credentials
client_id = 'a5ee82699bc543569b87d3f7cba0ff0a'
client_secret = '76649c9df8a04c13a7a9a4fa9d1e7517'

# Initialize Spotipy with client credentials
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Spotify URI for the playlist you want to access
playlist_uri = 'spotify:playlist:4pgDD1e5DGlTwJpHbUl4xO'

# Fetch playlist tracks
def get_playlist_tracks(playlist_uri):
    results = sp.playlist_items(playlist_uri)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks

# Print tracks and save them to a file
def print_and_save_tracks(tracks, file_name='bass.txt'):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i, item in enumerate(tracks):
            track = item['track']
            track_info = f"{track['name']} - {', '.join([artist['name'] for artist in track['artists']])}\n"
            print(track_info, end='')
            file.write(track_info)

# Main function
if __name__ == "__main__":
    tracks = get_playlist_tracks(playlist_uri)
    print_and_save_tracks(tracks)
