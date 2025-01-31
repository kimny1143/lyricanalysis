import lyricsgenius
import os
import time
from dotenv import load_dotenv

load_dotenv()
genius_access_token = os.getenv("GENIUS_ACCESS_TOKEN")
genius = lyricsgenius.Genius(genius_access_token, sleep_time=0.2, retries=3)

# 曲名とアーティスト名を入力して歌詞を取得
while True:
    song_query = input("曲名を入力してください: ")
    artist_query = input("アーティスト名を入力してください: ")
    song = genius.search_song(song_query, artist=artist_query)
    if song:
        confirm = input(f"この曲ですか？ {song.title} by {song.artist} (Y/N): ")
        if confirm.lower() == 'y':
            print(song.lyrics)
            break
    else:
        retry = input("曲が見つかりませんでした、もう一度検索しますか？ (Y/N): ")
        if retry.lower() != 'y':
            break

# アーティスト名を入力してアーティストの曲を取得
confirm = input("楽曲リストを取得しますか？ (Y/N): ")
if confirm.lower() != 'y':
    print("アプリを終了します。")
    exit()
artist_name = input("アーティスト名を入力してください: ")
max_songs = int(input("取得する曲の最大数を入力してください: "))

try:
    artist = genius.search_artist(artist_name, max_songs=max_songs)
    print(artist.songs)
except Exception as e:
    print(f"Error: {e}")
    time.sleep(60)  # レート制限に達した場合、1分待機