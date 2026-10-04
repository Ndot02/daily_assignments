

prices = {"tea": 20, "coffee": 50, "samosa": 25}
print("Menu:", prices)

item = input("What do you want? ")
qty  = int(input("How many? "))

price = prices.get(item, 0)
print("Price of one:", price)
print("Total bill  :", price * qty)

# Your job:
# 1. add "momo": 150 to the menu
prices["momo"]=150
# 2. print the cheapest and costliest price
print(f"The cheapest prices is {min(prices.values())}")
print(f"The costliest price is {max(prices.values())}")

# 3. print item names A-Z with sorted(prices)
print("Items:",sorted(prices))