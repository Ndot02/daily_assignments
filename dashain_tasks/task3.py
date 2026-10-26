kites = ["red", "blue", "green"]
# 01
# Add "yellow" at the end and "black" at the start
# 02
# Remove "green". Then pop() the last kite and print it as sold
# 03
# Sort the list. Print the first two kites with slicing
# 04
# Print how many kites are left, and whether "blue" is in stock
# 05
# Turn "pink,orange,white" into a list with split() and add it
# 06
# Print all kites joined with " | "
# 07
# Make a real copy, add "gold" to it, show the original did not change
# 08
# With prices = [["small", 50], ["big", 150]], print the big kite's price

kites.append("yellow")
kites[0]="black"
kites.sort()

print(kites[:2])
print(f"How many?:{len(kites)}")
print(f"have blue?:{"blue" in kites}")

new = "pink,orange,white".split(",")
kites.extend(new)
print(" | ".join(kites))

backup= kites.copy()
kites.append("gold")
print(backup)
print(kites)

prices = [["small", 50], ["big", 150]]
print("Big kite price:", prices[1][1])