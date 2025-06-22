import spotipy
from spotipy.oauth2 import SpotifyOAuth

import creds
import playlists
import tracks
import users

#Authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=creds.CLIENT_ID, client_secret= creds.CLIENT_SECRET, redirect_uri=creds.REDIRECT_URI, scope=creds.ADMIN_SCOPE))
# users.get_current_user(sp)
# users.get_artists_followed_by_current_user(sp)
# playlists.get_current_user_playlists(sp)
# playlists.get_playlist_items(sp, '1WVenIVDCjENnGkxTYMOHs')
# tracks.get_current_user_saved_tracks(sp)
# tracks.get_track_audio_analysis(sp, '3rXoaocGAOEq6CorwCiI4J')
# tracks.get_track_audio_features(sp, ['3rXoaocGAOEq6CorwCiI4J'])
# tracks.get_recommendations(sp, [], [], ['3rXoaocGAOEq6CorwCiI4J'])
# playlists.create_playlist(sp, 'mccurrymitchell', 'Test Playlist', 'Playlist created by code')
# playlists.add_items_to_playlist(sp, '6TG4cq5LziYdyZF1XhUoEF', ['3rXoaocGAOEq6CorwCiI4J'])
users.get_top_artists(sp)
