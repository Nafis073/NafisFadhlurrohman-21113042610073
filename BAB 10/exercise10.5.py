from pathlib import Path

path = Path("guest_book.txt")

while True:
    name = input("Masukkan nama (ketik 'quit' untuk selesai): ")

    if name.lower() == "quit":
        break

    contents = f"Selamat datang, {name}!\n"
    with path.open("a") as file:
        file.write(contents)

    print(f"Terima kasih, {name}.")