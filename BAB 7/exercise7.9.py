sandwich_orders = [
    "Tuna",
    "Pastrami",
    "Chicken",
    "Pastrami",
    "Beef",
    "Pastrami"
]

finished_sandwiches = []

print("Pastrami sedang habis.")

while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print(f"Membuat sandwich {sandwich}.")
    finished_sandwiches.append(sandwich)

print("\nSandwich selesai:")

for sandwich in finished_sandwiches:
    print(sandwich)