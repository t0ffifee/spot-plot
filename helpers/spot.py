from time import sleep
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import os

def get_playlist_ids(sp):
    """
    returns the IDs of the user's playlists
    """
    results = sp.current_user_playlists()
    ids = [r['id'] for r in results['items']]
    return ids    

def get_playlist_track_metas(sp, playlist_id):
    """
    returns the names, artists and IDs of the tracks in the playlist
    """
    offset = 0
    ids = []
    fields = 'items.track.id, items.track.name, items.track.artists, total'
    while True:
        response = sp.playlist_items(playlist_id,
                                    offset=offset,
                                    fields=fields,
                                    additional_types=['track'])
        
        if len(response['items']) == 0:
            break
        
        ids += response['items']
        offset = offset + len(response['items'])
    return ids

def parse_ids(playlist_tracks):
    ids = []
    for track in playlist_tracks:
        try:
            id = track['track']['id']
            ids.append(id)
        except:
            continue
    return ids

def get_playlist_tracks(sp, playlist_id):
    results = sp.playlist_tracks(playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks

def get_audio_analysis(sp, tracks):
    track_analysis = []
    i = 0
    while True:
        try:
            analysis = sp.audio_analysis(tracks[i])
            track_analysis += analysis
            
            i += 1
            if i >= len(tracks):
                break
        except:
            sleep(2)
    return track_analysis

def get_audio_features(sp, track_ids):
    track_features = []
    start, end = 0, 100
    # fields = 'danceability, energy, key, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo'
    while True:
        try:
            ts = track_ids[start:end]
            features = sp.audio_features(ts)
            track_features += features

            start += 100
            end += 100
            if start >= len(track_ids):
                break
        except:
            sleep(2)
    return track_features

def parse_metas(playlist_tracks, METAS):
    track_metas = []
    for item in playlist_tracks:
        try:
            track = item['track']
            m = [track[key] for key in METAS]
            track_metas.append(m)
        except:
            continue
    return track_metas

def parse_features(track_features_mess, FEATURES):
    track_features = []
    for track in track_features_mess:
        try:
            f = [track[key] for key in FEATURES]
            d = dict(zip(FEATURES, f))
            track_features.append(d)
        except:
            continue
    return track_features

def setup():
    client_id = os.environ.get('SPOT_CLIENT_ID')
    secret = os.environ.get('SPOT_SECRET')
    redirect = 'https://localhost/'
    scope = "playlist-read-private"

    auth_manager = SpotifyOAuth(scope=scope, client_id=client_id, client_secret=secret, redirect_uri=redirect)
    sp = spotipy.Spotify(auth_manager=auth_manager)
    return sp