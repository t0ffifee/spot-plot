import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

client_id = os.environ.get('SPOT_CLIENT_ID')
secret = os.environ.get('SPOT_SECRET')

auth_manager = SpotifyClientCredentials(client_id, secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

id = '0Fa3x3yr0duQJStzGpnH7w'
# fields = ['tracks']

def get_playlist_tracks(playlist_id):
    results = sp.playlist_tracks(playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks

print(len(get_playlist_tracks(id)))
