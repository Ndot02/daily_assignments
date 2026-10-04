
name = input("Name: ")
age  = input("Age: ")
city = input("City: ")

student = (name, age, city)     # packing
n, a, c = student                # unpacking

print("===== ID CARD =====")
print("Name:", n)
print("Age :", a)
print("City:", c)

marks = (70, 85, 90)
# Your job: print max, min and sum of marks
print(f"The maximum no in tuple is {max(marks)}")
print(f"The minimum no in tuple is {min(marks)}")
print(f"The sum of tuple is {sum(marks)}")


# Your job: change the city (list, edit, tuple)
student = list(student)
student[2] = "Pokhara"
student = tuple(student)

print("Updated student:", student)