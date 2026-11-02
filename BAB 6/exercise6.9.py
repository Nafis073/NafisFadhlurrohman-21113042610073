favorite_places = {
    "Andi": ["Bali", "Lombok"],
    "Budi": ["Jepang", "Korea"],
    "Citra": ["Paris", "Swiss", "Italia"]
}

for name, places in favorite_places.items():
    print(f"Tempat favorit {name}:")

    for place in places:
        print(f"- {place}")

    print()