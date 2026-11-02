unprinted_designs = [
    "Desain Robot",
    "Desain Pesawat",
    "Desain Mobil"
]

completed_models = []

def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        print(f"Mencetak: {current_design}")

        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nModel yang selesai dicetak:")

    for model in completed_models:
        print(model)

print_models(unprinted_designs, completed_models)

show_completed_models(completed_models)