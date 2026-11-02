favorite_languages = {
    "Andi": "Python",
    "Budi": "Java",
    "Citra": "C++",
    "Dina": "Python"
}

people = ["Andi", "Budi", "Eko", "Fajar", "Dina"]

for person in people:
    if person in favorite_languages:
        print(f"Terima kasih {person}, sudah mengikuti polling.")
    else:
        print(f"{person}, silakan ikuti polling.")