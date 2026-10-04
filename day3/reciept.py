item     = input("Item name: ")
price    = float(input("Price: "))
quantity = int(input("Quantity: "))

subtotal = price * quantity

total = subtotal * 1.13

print(f"--- Receipt ---")
print(f"{quantity} x {item}= {subtotal}")
print(f"Total amount: {total}")