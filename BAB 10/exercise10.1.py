from pathlib import Path

path = Path("learning_python.txt")

# Membaca seluruh isi file
contents = path.read_text()
print("Membaca seluruh file:")
print(contents)

# Membaca file per baris
print("Membaca file per baris:")
for line in contents.splitlines():
    print(line)