

contacts = {"Ram": "9801111111", "Sita": "9802222222"}

name  = input("New contact name: ")
phone = input("Phone number: ")
contacts[name] = phone              # add it

print("All contacts:", contacts)
print("Total:", len(contacts))

find = input("Search a name: ")
print("Number:", contacts.get(find, "Not found"))

# Your job:
# 1. remove one contact with pop()
popped=contacts.pop("Sita")
print(f"removed number:{popped}")
# 2. print only the names: list(contacts.keys())
print(list(contacts.keys()))