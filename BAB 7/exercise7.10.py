responses = {}

polling_active = True

while polling_active:
    name = input("Siapa nama Anda? ")
    place = input("Ke mana tempat liburan impian Anda? ")

    responses[name] = place

    repeat = input("Apakah ada orang lain? (yes/no): ")

    if repeat.lower() == "no":
        polling_active = False

print("\nHasil polling:")

for name, place in responses.items():
    print(f"{name} ingin berlibur ke {place}.")