
menu = {"tea": 20, "coffee": 50, "momo": 150}
print("Menu:", menu)

item = input("What do you want? ").strip().lower()

if item in menu:
    qty = int(input("How many? "))
    if qty >= 500:
        total = menu[item] * qty*0.9
    elif qty >= 200:
        total= menu[item]*qty*0.95
    else:
        total= menu[item]*qty
    print(f"Total: Rs. {total}")
else:
    print("Sorry, we don't have that")

# Your job (inside the if block):
# 500 or more -> 10% off, 200 or more -> 5% off,
# else no discount. Print the final bill.