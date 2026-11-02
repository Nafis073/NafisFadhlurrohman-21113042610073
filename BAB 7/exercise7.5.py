while True:
    age = input("Masukkan umur Anda (atau quit): ")

    if age == "quit":
        break

    age = int(age)

    if age < 3:
        print("Tiket gratis.")
    elif age <= 12:
        print("Harga tiket 10 dolar.")
    else:
        print("Harga tiket 15 dolar.")