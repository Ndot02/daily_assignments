chart = [
    ["Empty", "Empty", "Empty", "Empty"],
    ["Empty", "Empty", "Empty", "Empty"],
    ["Empty", "Empty", "Empty", "Empty"],
]

name = input("Student name: ")
row = int(input("Row (0-2): "))
col = int(input("Column (0-3): "))
chart[row][col] = name
empty_count=0

for r in chart:
    print(r)

# "cm"># Your job: count empty seats — add up row.count("Empty") for every row
for row in chart:
    empty_count+=row.count("Empty") 
print(f"The total no of empty seats are {empty_count}")