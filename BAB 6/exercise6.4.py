glossary = {
    "variable": "Tempat menyimpan data.",
    "string": "Tipe data berupa teks.",
    "list": "Kumpulan elemen data.",
    "loop": "Perulangan dalam program.",
    "dictionary": "Pasangan key dan value.",
    "integer": "Tipe data bilangan bulat.",
    "float": "Tipe data bilangan desimal.",
    "boolean": "Tipe data True atau False.",
    "function": "Blok kode yang dapat digunakan kembali.",
    "tuple": "Kumpulan data yang tidak dapat diubah."
}

for word, meaning in glossary.items():
    print(f"{word.title()}:")
    print(f"  {meaning}\n")