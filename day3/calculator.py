num1 = float(input("First number: "))
num2 = float(input("Second number: "))

print("1) Add  2) Subtract  3) Multiply  4) Divide")
choice = input("Choose an operation: ")


match choice:
    case "1":
        print(f"{num1 + num2:.2f}")
    case "2":
        print(f"{num1 - num2:.2f}")
    case "3":
        print(f"{num1*num2:.2f}")
    case "4":
        print(f"{num1/num2:.2f}")
    case _:
        print("Invalid choice")