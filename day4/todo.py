

tasks = []

task = input("Add a task (or 'quit'): ")

while task != "quit":
    tasks.append(task)
    task = input("Add a task (or 'quit'): ")

count = 1

for t in tasks:
    print(f"{count}. {t}")
    count += 1

# Remove a task
remove = int(input("Enter task number to remove: "))

removed_task = tasks.pop(remove - 1)

print(f"Removed: {removed_task}")

print("\nRemaining tasks:")

count = 1
for t in tasks:
    print(f"{count}. {t}")
    count += 1