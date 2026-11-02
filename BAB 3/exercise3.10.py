places = ["Bandung", "Jakarta", "Surabaya"]

print("Daftar awal:", places)

places.append("Semarang")
print("Setelah append:", places)

places.insert(1, "Yogyakarta")
print("Setelah insert:", places)

places.remove("Jakarta")
print("Setelah remove:", places)

places.pop()
print("Setelah pop:", places)

places.sort()
print("Setelah sort:", places)

places.reverse()
print("Setelah reverse:", places)

print("Jumlah tempat:", len(places))