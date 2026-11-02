cities = {
    "Jakarta": {
        "country": "Indonesia",
        "population": 10600000,
        "fact": "Merupakan ibu kota terbesar di Indonesia."
    },

    "Tokyo": {
        "country": "Jepang",
        "population": 14000000,
        "fact": "Memiliki sistem transportasi yang maju."
    },

    "Paris": {
        "country": "Prancis",
        "population": 2100000,
        "fact": "Terkenal dengan Menara Eiffel."
    }
}

for city, information in cities.items():
    print(f"Kota: {city}")
    print(f"Negara: {information['country']}")
    print(f"Populasi: {information['population']}")
    print(f"Fakta: {information['fact']}\n")