def get_current_user_playlists(sp):
    playlists = sp.current_user_playlists(limit=50)
    total_playlists = playlists['total']
    items = playlists['items']
    print("Total number of playlists: ", total_playlists)
    for playlist in items:
        id = playlist['id']
        name = playlist['name']
        print("Playlist Name: ", name)
        print("Playlist ID: ", id)

def get_playlist_items(sp, playlist_id):
    playlist_items = sp.playlist_items(playlist_id, limit=1)
    total_playlist_items = playlist_items['total']
    print('Total items in playlist: ', total_playlist_items)
    items = playlist_items['items']
    for item in items:
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

def create_playlist(sp, user, name, description):
    new_playlist = sp.user_playlist_create(user=user, name=name, public=True, collaborative=False, description=description)
    playlist_id = new_playlist['id']
    print('Playlist ID: ', playlist_id)

def add_items_to_playlist(sp, playlist_id, items):
    snapshot_id = sp.playlist_add_items(playlist_id, items, position=None)
    print(snapshot_id)
