sandwich_orders = [
    "Tuna Sandwich",
    "Chicken Sandwich",
    "Beef Sandwich"
]

finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"Sandwich {current_sandwich} sedang dibuat.")

    finished_sandwiches.append(current_sandwich)

print("\nSandwich yang selesai:")

for sandwich in finished_sandwiches:
    print(sandwich)