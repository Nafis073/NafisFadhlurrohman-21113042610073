favorite_numbers = {
    "Andi": [7, 10],
    "Budi": [5, 15],
    "Citra": [3, 8, 12],
    "Dina": [21, 25],
    "Eko": [4, 9]
}

for name, numbers in favorite_numbers.items():
    print(f"Angka favorit {name}:")

    for number in numbers:
        print(number)

    print()