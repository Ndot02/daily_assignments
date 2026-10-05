

num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
if num>10:
    print("Big number")
elif num>1 and num<10:
    print("small number")
else:
    print()
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

# Your job:
# 1. if num is more than 100, print "Big number"
# 2. if num is from 1 to 10 (use and), print "Small number"