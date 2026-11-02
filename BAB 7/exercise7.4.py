prompt = "Masukkan topping pizza:"
prompt += "\nKetik 'quit' untuk selesai. "

while True:
    topping = input(prompt)

    if topping == "quit":
        break
    else:
        print(f"Topping {topping} ditambahkan.")