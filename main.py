import requests
from ytmusicapi import YTMusic
from bs4 import BeautifulSoup
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

user_choice = input("Which year do you want to travel to? Enter in this format YYYY-MM-DD ")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{user_choice}", headers=header)
song_page = response.text
soup = BeautifulSoup(song_page, "html.parser")

song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

print(song_names)

yt = YTMusic("browser.json")

playlists = yt.get_library_playlists()
print(f"Found {len(playlists)} playlists in your library.")

PLAYLIST_NAME = f"{user_choice} Billboard 100"

playlist_id = None
playlists = yt.get_library_playlists(limit=100)

for p in playlists:
    if p["title"] == PLAYLIST_NAME:
        playlist_id = p["playlistId"]
        break

if playlist_id:
    print("This playlist already exists.")
else:
    playlist_id = yt.create_playlist(
        PLAYLIST_NAME,
        f"Playlist with the hottest songs from {user_choice}",
        privacy_status="PRIVATE",
    )
    print("Playlist created.")

for song in song_names:
    try:
        search_results = yt.search(song, filter="songs", limit=1)
        yt.add_playlist_items(playlist_id, [search_results[0]["videoId"]])
        print(f"Added: {song}")
    except Exception as e:
        print(f"Skipped: {song} | Reason: {e}")
