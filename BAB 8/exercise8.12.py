def make_sandwich(*ingredients):
    print("Sandwich dibuat dengan bahan:")

    for ingredient in ingredients:
        print(f"- {ingredient}")

make_sandwich("Keju", "Tomat")

print()

make_sandwich("Ayam", "Selada", "Mayones")

print()

make_sandwich("Telur", "Keju", "Sosis", "Saus")