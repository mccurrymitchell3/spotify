def get_current_user(sp):
    user = sp.current_user()
    country = user['country']
    display_name = user['display_name']
    email = user['email']
    id = user['id']
    total_followers = user['followers']['total']
    print(user)
    print("Country: ", country)
    print("Display Name: ", display_name)
    print("Email: ", email)
    print("User ID: ", id)
    print("Total followers: ", total_followers)

def get_artists_followed_by_current_user(sp):
    artists = sp.current_user_followed_artists(limit=50, after=None)
    artists = artists['artists']
    total_artists_followed = artists['total']
    items = artists['items']
    print('Total number of artists I follow: ', total_artists_followed)
    for artist in items:
        name = artist['name']
        follower_count = artist['followers']['total']
        genres = artist['genres']
        id = artist['id']
        popularity = artist['popularity']
        print('Artist Name: ', name)
        print('Artist Follower Count: ', follower_count)
        print('Artist Genres: ', genres)
        print('Artist ID: ', id)
        print('Artist Popularity: ', popularity)

def get_top_artists(sp):
    top_artists = sp.current_user_top_artists(limit=50, offset=0, time_range='medium_term')
    total_artists = top_artists['total']
    items = top_artists['items']
    print(total_artists)
    for item in items:
        artist_name = item['name']
        artist_popularity = item['popularity']
        artist_id = item['id']
        artist_genres = item['genres']
        print('Name: ', artist_name)
        print('Popularity: ', artist_popularity)
        print('Genres: ', artist_genres)
        print('Artist ID: ', artist_id)
