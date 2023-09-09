from bs4 import BeautifulSoup
import requests
import os
import pprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth


SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")

time = input("Which year do you want to travel to ? Type the date in this format YYYY-MM-DD")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{time}")
soup_page = BeautifulSoup(response.text, "html.parser")
song_names_spans = [song.text.strip() for song in soup_page.select("li ul li h3")]
print(song_names_spans)

spotify = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri="http://example.com",
        scope="playlist-modify-public"
    )
)

song_uris = []
year = time.split("-")[0]
current_spotify_user = spotify.current_user()

for song in  song_names_spans:
    result = spotify.search(q=f"track:{song} year:{year}", type="track")
    # pprint.pprint(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
playlist_name = f"{time} Billboard 100"
current_spotify_user_id = current_spotify_user["id"]
print(current_spotify_user_id)
playlist = spotify.user_playlist_create(
    user=current_spotify_user_id,
    name=playlist_name,
    description="Song from 100 Billboard"
)
# spotify.playlist_add_items()
playlist_id = playlist["id"]
print(playlist)
result = spotify.playlist_add_items(playlist_id=playlist_id, items=song_uris)
print(result)