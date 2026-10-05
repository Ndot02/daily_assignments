users = {"ram": "ram123", "sita": "sita456"}
users["nirajan"]=""
name = input("Username: ").strip().lower()
password = input("Password: ")

if name not in users:
    print("User not found")
elif users[name]=="":
        print("Password missing")
elif users[name] == password:
    print(f"Welcome, {name.title()}!")
else:
    print("Wrong password")

# Your job:
# 1. add yourself to the users dictionary
# 2. empty password? print "Password missing"