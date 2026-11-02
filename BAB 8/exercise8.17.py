def calculate_total(price, quantity):
    """Menghitung total harga berdasarkan jumlah barang."""
    total = price * quantity
    return total


product_price = 15000
product_quantity = 3

total_price = calculate_total(
    product_price,
    product_quantity
)

print(f"Total harga: Rp{total_price}")