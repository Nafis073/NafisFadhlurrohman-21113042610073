def make_album(artist, title, songs=None):
    album = {
        "artist": artist,
        "title": title
    }

    if songs is not None:
        album["songs"] = songs

    return album

album1 = make_album("Taylor Swift", "1989")
album2 = make_album("Adele", "25")
album3 = make_album("Coldplay", "Parachutes", 10)

print(album1)
print(album2)
print(album3)