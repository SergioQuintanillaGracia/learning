import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

SPOTIFY_CLIENT_ID = "..."
SPOTIFY_CLIENT_SECRET = "..."

date = input("Which year do you want to travel to? Type the date in the format YYYY-MM-DD: ")

url = f"https://www.billboard.com/charts/hot-100/{date}/"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:139.0) Gecko/20100101 Firefox/139.0"
}

response = requests.get(url, headers=headers)
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
titles = soup.select(selector="ul li ul li h3")
titles = [title.text.strip() for title in titles]

scope = "playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET, redirect_uri="https://example.com"))

track_ids = []
for track in titles:
    response = sp.search(q=track, type="track", limit=1)
    tracks = response["tracks"]["items"]

    if tracks:
        track_id = tracks[0]["id"]
        track_ids.append(track_id)

    print(f"Searching {track}")

print("Creating playlist...")
user_id = sp.current_user()["id"]
response = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
playlist_id = response["id"]

print("Adding songs...")
sp.playlist_add_items(playlist_id=playlist_id, items=track_ids)