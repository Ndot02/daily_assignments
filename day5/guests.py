

ram  = set(input("Ram's guests: ").split(","))
sita = set(input("Sita's guests: ").split(","))

print("On both lists:", ram & sita)
print("All guests   :", ram | sita)

# Your job:
# 1. print total guests using len()
print(f"Total guest: {len(ram|sita)}")
# 2. print guests only Ram invited (ram - sita)
print(f"Total guest only ram invited: {len(ram-sita)}")

print("Is Hari invited?", "Hari" in ram)

# 4. add a guest, discard a guest, print again
ram.add("sam")
ram.discard("gita")
print("Ram's updated guests:", ram)