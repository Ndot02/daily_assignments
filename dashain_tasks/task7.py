def get_average(marks):
      return round(sum(marks) / len(marks), 2)

def get_grade(avg):
    if avg >= 80:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 40:
        return "C"
    return "Fail"
def report(name, marks, pass_mark=40):
    avg = get_average(marks)
    print(f"{name}: avg {avg}, grade {get_grade(avg)}")
    print("  Best:", max(marks), "| Worst:", min(marks))
    print("  Passed all?", min(marks) >= pass_mark)

names = ["Sita", "Ram", "Gita"]
all_marks = [[90, 85, 78], [45, 38, 60], [70, 65, 80]]

for name, marks in zip(names, all_marks):
    report(name, marks)

averages = []
for marks in all_marks:
    averages.append(get_average(marks))

for rank, avg in enumerate(sorted(averages, reverse=True), start=1):
    print(f"Rank {rank}: {avg}")