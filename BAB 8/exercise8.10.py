messages = [
    "Selamat pagi!",
    "Semangat belajar!",
    "Jangan lupa makan."
]

sent_messages = []

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()

        print(f"Mengirim pesan: {current_message}")

        sent_messages.append(current_message)

send_messages(messages, sent_messages)

print("\nPesan yang belum terkirim:", messages)
print("Pesan yang sudah terkirim:", sent_messages)