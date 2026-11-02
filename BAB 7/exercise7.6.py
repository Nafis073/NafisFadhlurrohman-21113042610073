prompt = "Masukkan topping: "
prompt += "\nKetik quit untuk berhenti. "

topping = ""

while topping != "quit":
    topping = input(prompt)

    if topping != "quit":
        print(f"{topping} ditambahkan.")