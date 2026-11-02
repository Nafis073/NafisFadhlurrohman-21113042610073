current_users = ["Andi", "Budi", "Citra", "Dina", "Eko"]

new_users = ["andi", "Fajar", "Gita", "budi", "Hani"]

current_users_lower = [
    user.lower() for user in current_users
]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"{new_user} sudah digunakan. Pilih nama lain.")
    else:
        print(f"{new_user} tersedia.")