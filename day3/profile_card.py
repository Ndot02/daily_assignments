name       = input("Full name: ").strip().title()
birth_year = int(input("Birth year: "))

age = 2026 - birth_year
is_long_name = len(name) > 10

print(f"Name: {name.upper()}")
print(f"Age: {age}")

if(is_long_name):
    print("your name is long")