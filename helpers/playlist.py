from time import sleep

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
            if i >= len(tracks):
                break
            i += 1
        except:
            sleep(2)

    return track_analysis

def get_audio_features(sp, tracks):
    track_features = []
    start, end = 0, 100
    while True:
        try:
            ts = tracks[start:end]
            features = sp.audio_features(ts)
            track_features.append(features)
            if start >= len(tracks):
                break
            start += 100
            end += 100
        except:
            sleep(2)

        