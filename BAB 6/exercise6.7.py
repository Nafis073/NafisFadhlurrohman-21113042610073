person_1 = {
    "first_name": "Andi",
    "last_name": "Saputra",
    "age": 20,
    "city": "Solo"
}

person_2 = {
    "first_name": "Budi",
    "last_name": "Santoso",
    "age": 21,
    "city": "Yogyakarta"
}

person_3 = {
    "first_name": "Citra",
    "last_name": "Putri",
    "age": 19,
    "city": "Semarang"
}

people = [person_1, person_2, person_3]

for person in people:
    print(f"Nama: {person['first_name']} {person['last_name']}")
    print(f"Umur: {person['age']}")
    print(f"Kota: {person['city']}\n")