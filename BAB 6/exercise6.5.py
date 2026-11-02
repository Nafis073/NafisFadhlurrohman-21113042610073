rivers = {
    "Nil": "Mesir",
    "Amazon": "Brasil",
    "Gangga": "India"
}

print("Informasi sungai:")

for river, country in rivers.items():
    print(f"Sungai {river} mengalir melalui {country}.")

print("\nNama sungai:")

for river in rivers.keys():
    print(river)

print("\nNama negara:")

for country in rivers.values():
    print(country)