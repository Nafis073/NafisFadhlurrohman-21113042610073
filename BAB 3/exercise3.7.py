guests = ["Eko", "Andi", "Fajar", "Dina", "Citra", "Gita"]

while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Maaf {removed_guest}, undangan dibatalkan.")
    
for guest in guests:
    print(f"{guest}, kamu tetap diundang.")
    
del guests[0]
del guests[0]

print("Daftar Tamu:", guests)