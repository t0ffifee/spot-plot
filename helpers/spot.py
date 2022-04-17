from time import sleep

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
            track_analysis.append(analysis)
            
            i += 1
            if i >= len(tracks):
                break
        except:
            sleep(2)
    return track_analysis

def get_audio_features(sp, track_ids):
    track_features = []
    start, end = 0, 100
    while True:
        try:
            ts = track_ids[start:end]
            features = sp.audio_features(ts)
            track_features.append(features)

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
            track_features.append(f)
        except:
            continue
    return track_features