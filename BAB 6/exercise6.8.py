pet_1 = {
    "animal": "Kucing",
    "owner": "Andi"
}

pet_2 = {
    "animal": "Anjing",
    "owner": "Budi"
}

pet_3 = {
    "animal": "Kelinci",
    "owner": "Citra"
}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print(f"Hewan: {pet['animal']}")
    print(f"Pemilik: {pet['owner']}\n")