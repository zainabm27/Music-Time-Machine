# 🎵 Music Time Machine

A Python automation project that recreates Billboard Hot 100 playlists from any selected date on YouTube Music.

## Features

- Scrapes Billboard Hot 100
- Retrieves the Top 100 songs
- Creates a private YouTube Music playlist
- Automatically adds songs
- Prevents duplicate playlists

## Technologies

- Python
- Requests
- BeautifulSoup
- YTMusicAPI

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

Enter a date in the format:

```
YYYY-MM-DD
```

Example:

```
2005-07-15
```

## Note

`browser.json` is required for YouTube Music authentication and is intentionally excluded from this repository.
