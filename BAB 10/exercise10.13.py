import json
from pathlib import Path

path = Path("user_data.json")

if path.exists():
    contents = path.read_text()
    user_data = json.loads(contents)

else:
    user_data = {}

    user_data["nama"] = input("Masukkan nama: ")
    user_data["umur"] = input("Masukkan umur: ")
    user_data["hobi"] = input("Masukkan hobi: ")

    contents = json.dumps(user_data)
    path.write_text(contents)

print("\nInformasi pengguna:")
print(f"Nama: {user_data['nama']}")
print(f"Umur: {user_data['umur']}")
print(f"Hobi: {user_data['hobi']}")