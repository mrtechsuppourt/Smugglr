from flask import Flask, render_template, request, jsonify
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

app = Flask(__name__)

# Set your Spotify API credentials
client_id = 'a5ee82699bc543569b87d3f7cba0ff0a'
client_secret = '76649c9df8a04c13a7a9a4fa9d1e7517'

# Initialize Spotipy with client credentials
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/getPlaylistTracks', methods=['GET'])
def get_playlist_tracks():
    playlist_uri = request.args.get('uri')

    if not playlist_uri:
        return jsonify({'error': {'message': 'Missing playlist URI'}}), 400

    try:
        results = sp.playlist_items(playlist_uri)
        tracks = results['items']
        while results['next']:
            results = sp.next(results)
            tracks.extend(results['items'])

        formatted_tracks = [{
            'name': track['track']['name'],
            'artists': [{'name': artist['name']} for artist in track['track']['artists']]
        } for track in tracks]

        return jsonify({'tracks': formatted_tracks})

    except Exception as e:
        return jsonify({'error': {'message': str(e)}}), 500

if __name__ == '__main__':
    app.run(debug=True)
