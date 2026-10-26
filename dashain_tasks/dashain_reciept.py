name,price,quantity=input("Enter name, price and quantity: ").split(",")
price= float(price)
quantity=int(quantity)

total= price*quantity
code=name[0:3].upper()

print("--Dashain Reciept")
print(f"Customer:{name.title()}")
print(f"Item:{name.upper()} (code:{code})")
print(f"Total:Rs{total:.2f}")
print(f"500 notes: {int(total // 500)}, left Rs {total % 500:.2f}")
print("Over 1000?", total > 1000)
print("Price type:", type(price))