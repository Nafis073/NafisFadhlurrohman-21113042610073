def make_album(artist, title):
    return {
        "artist": artist,
        "title": title
    }

while True:
    print("\nMasukkan informasi album.")

    print("(Masukkan q untuk berhenti)")

    artist = input("Nama artis: ")

    if artist.lower() == "q":
        break

    title = input("Judul album: ")

    if title.lower() == "q":
        break

    album = make_album(artist, title)

    print(album)