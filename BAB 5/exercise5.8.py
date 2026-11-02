usernames = ["admin", "andi", "budi", "citra", "dina"]

for username in usernames:
    if username == "admin":
        print("Halo admin, ingin melihat laporan status?")
    else:
        print(f"Halo {username.title()}, selamat datang kembali.")