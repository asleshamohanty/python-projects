import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy import Spotify, oauth2, client
from spotipy.oauth2 import SpotifyOAuth


date = input("Which day do you want to travel back to? Enter in this format: YYYY-MM-DD: ")

BILLBOARD_URL = f"https://www.billboard.com/charts/hot-100/{date}/"
OAUTH_TOKEN_URL= 'https://accounts.spotify.com/api/token'
spotify_oath_params = {
    "client_id": "20ccd357db48434abf49097407a91658",
    "client_secret": "191cd89b87b5442a8e9bf0d68f25642d",
    "redirect_uri": "http://example.com",
}


billboard_response = requests.get(BILLBOARD_URL)
billboard_page = billboard_response.text

soup = BeautifulSoup(billboard_page, "html.parser")
songs_data = soup.select("li ul li h3")
songs_list = [song.getText().strip() for song in songs_data]
print(songs_list)


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="20ccd357db48434abf49097407a91658",
        client_secret="191cd89b87b5442a8e9bf0d68f25642d",
        show_dialog=True,
        cache_path="token.txt",
        username="Musical Time Machine",
    )
)

sp_oauth = oauth2.SpotifyOAuth("20ccd357db48434abf49097407a91658","191cd89b87b5442a8e9bf0d68f25642d","http://example.com",scope="playlist-modify-private",cache_path="SpotifyProject/token.txt", show_dialog=True, username="Musical Time Machine" )
auth_url = sp_oauth.get_auth_response()
token = sp_oauth.get_cached_token()

user_id = sp.current_user()['id']
year = date.split('-')[0]

playlist = sp.user_playlist_create(user_id, name=f"{date} Billboard 100", public=False, description=f'Taking you back in time with the Top 100 songs of {date} !')
playlist_id = playlist["id"]

uri_list = []
for song in songs_list:
    tracks = sp.search(q=f'track:{song} year:{year}', type='track')

    try:
        uri = tracks['tracks']['items'][0]['uri']
        uri_list.append(uri)

    except IndexError:
        print(f'The song {song} is not on Spotify')

sp.playlist_add_items(playlist_id, uri_list)








# spotify = SpotifyOAuth
# spotify.get_authorize_url()
