from pathlib import Path

filenames = ["sample_text.txt"]

for filename in filenames:
    path = Path(filename)

    try:
        contents = path.read_text()

    except FileNotFoundError:
        print(f"File {filename} tidak ditemukan.")

    else:
        jumlah_the = contents.lower().count("the")
        jumlah_the_spasi = contents.lower().count("the ")

        print(f"File: {filename}")
        print(f"Jumlah kata 'the': {jumlah_the}")
        print(f"Jumlah kata 'the ': {jumlah_the_spasi}")