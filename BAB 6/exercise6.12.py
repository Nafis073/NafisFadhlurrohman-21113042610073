cities = {
    "Jakarta": {
        "country": "Indonesia",
        "population": 10600000,
        "language": "Bahasa Indonesia",
        "currency": "Rupiah"
    },

    "Tokyo": {
        "country": "Jepang",
        "population": 14000000,
        "language": "Bahasa Jepang",
        "currency": "Yen"
    }
}

for city, info in cities.items():
    print(f"Informasi Kota {city}")
    print(f"Negara: {info['country']}")
    print(f"Populasi: {info['population']}")
    print(f"Bahasa: {info['language']}")
    print(f"Mata uang: {info['currency']}\n")