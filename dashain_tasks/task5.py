name = input("Name: ").strip()
age = int(input("Age: "))
height = int(input("Height (cm): "))
code = input("Coupon code: ").strip().lower()

if not name:
    print("Please enter your name.")
elif age < 5 or height < 110:
    print(f"Sorry {name}, the big ping is not safe for you.")
else:
    if age >= 60:
        price = 0
    elif age < 12:
        price = 50
    else:
        price = 100

    if code in ["dashain", "tihar"] and price > 0:
        price = price - 20
        print("Coupon used! Rs 20 off.")

    print(f"{name}, your ping ticket is Rs {price}.")