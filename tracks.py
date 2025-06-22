def get_current_user_saved_tracks(sp):
    saved_tracks = sp.current_user_saved_tracks(limit=1)
    total_saved_tracks = saved_tracks['total']
    items = saved_tracks['items']
    for item in items:
        added_at = item['added_at']
        track = item['track']
        track_duration = track['duration_ms']
        track_id = track['id']
        track_name = track['name']
        track_popularity = track['popularity']
        track_artists = track['artists']
        print('Track Name: ', track_name)
        print('Track ID: ', track_id)
        print('Track Popularity: ', track_popularity)
        print('Track Duration: ', track_duration)
        print('Track Added Date: ', added_at)
        print('Track Artists: ')
        for artist in track_artists:
            artist_id = artist['id']
            artist_name = artist['name']
            print(' - ' + artist_name)
            print(' - ' + artist_id)
        album = track['album']
        album_id = album['id']
        album_name = album['name']
        album_release_date = album['release_date']
        print('Album Name: ', album_name)
        print('Album ID: ', album_id)
        print('Album Release Date: ', album_release_date)
        album_artists = album['artists']
        print('Album Artists: ')
        for artist in album_artists:
            artist_id = artist['id']
            artist_name = artist['name']
            print(' - ' + artist_name)
            print(' - ' + artist_id)

def get_track_audio_analysis(sp, track_id):
    audio_analysis = sp.audio_analysis(track_id)
    track = audio_analysis['track']
    track_duration = track['duration']
    track_end_of_fade_in = track['end_of_fade_in']
    track_start_of_fade_out = track['start_of_fade_out']
    track_loudness = track['loudness']
    track_tempo = track['tempo']
    track_tempo_confidence = track['tempo_confidence']
    track_time_signature = track['time_signature']
    track_time_signature_confidence = track['time_signature_confidence']
    track_key = track['key']
    track_key_confidence = track['key_confidence']
    track_mode = track['mode']
    track_mode_confidence = track['mode_confidence']
    print('Track Duration: ', track_duration)
    print('Track End of Fade in: ', track_end_of_fade_in)
    print('Track Start of Fade out: ', track_start_of_fade_out)
    print('Track Loudness: ', track_loudness)
    print('Track Tempo: ', track_tempo)
    print('Track Tempo Confidence: ', track_tempo_confidence)
    print('Track Time Signature: ', track_time_signature)
    print('Track Time Signature Confidence: ', track_time_signature_confidence)
    print('Track Key: ', track_key)
    print('Track Key Confidence: ', track_key_confidence)
    print('Track Mode: ', track_mode)
    print('Track Mode Confidence: ', track_mode_confidence)

def get_track_audio_features(sp, track_ids):
    audio_features = sp.audio_features(tracks=track_ids)
    for track_audio_features in audio_features:
        danceability = track_audio_features['danceability']
        energy = track_audio_features['energy']
        key = track_audio_features['key']
        loudness = track_audio_features['loudness']
        mode = track_audio_features['mode']
        speechiness = track_audio_features['speechiness']
        acousticness = track_audio_features['acousticness']
        instrumentalness = track_audio_features['instrumentalness']
        liveness = track_audio_features['liveness']
        valence = track_audio_features['valence']
        tempo = track_audio_features['tempo']
        track_id = track_audio_features['id']
        duration_ms = track_audio_features['duration_ms']
        time_signature = track_audio_features['time_signature']
    print('Daceability: ', danceability)
    print('Energy: ', energy)
    print('Key: ', key)
    print('Loudness: ', loudness)
    print('Mode: ', mode)
    print('Speechiness: ', speechiness)
    print('Acousticness: ', acousticness)
    print('Instrumentalness: ', instrumentalness)
    print('Liveness: ', liveness)
    print('Valence: ', valence)
    print('Tempo: ', tempo)
    print('Track ID: ', track_id)
    print('Duration in ms: ', duration_ms)
    print('Time Signature: ', time_signature)

def get_recommendations(sp, seed_artists, seed_genres, seed_tracks):
    recommendations = sp.recommendations(seed_artists=seed_artists, seed_genres=seed_genres, seed_tracks=seed_tracks, limit=5, country=None)
    tracks = recommendations['tracks']
    for track in tracks:
        track_duration = track['duration_ms']
        track_id = track['id']
        track_name = track['name']
        track_popularity = track['popularity']
        track_artists = track['artists']
        print('Track Name: ', track_name)
        print('Track ID: ', track_id)
        print('Track Popularity: ', track_popularity)
        print('Track Duration: ', track_duration)
        print('Track Artists: ')
        for artist in track_artists:
            artist_id = artist['id']
            artist_name = artist['name']
            print(' - ' + artist_name)
            print(' - ' + artist_id)
        album = track['album']
        album_id = album['id']
        album_name = album['name']
        album_release_date = album['release_date']
        print('Album Name: ', album_name)
        print('Album ID: ', album_id)
        print('Album Release Date: ', album_release_date)
        album_artists = album['artists']
        print('Album Artists: ')
        for artist in album_artists:
            artist_id = artist['id']
            artist_name = artist['name']
            print(' - ' + artist_name)
            print(' - ' + artist_id)
