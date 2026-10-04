

name = input("Student name: ")
m1 = int(input("Math: "))
m2 = int(input("Science: "))
m3 = int(input("English: "))

subjects = ["math", "science", "english"]
marks  = dict(zip(subjects, [m1, m2, m3]))
report = {"name": name, "marks": marks}

print("===== REPORT CARD =====")
print("Name :", report["name"])
print("Marks:", report["marks"])

# Your job:
total = sum(marks.values())

average= total / len(marks)
best_subject= max(marks, key=marks.get)

print(f"The total marks is {total}")
print(f"The average is {average}")
print("The best subject is ",best_subject)
