n = int(input("Enter number of students: "))

marks = [0] * n
reg_nos = [0] * n

for i in range(n):
    reg_nos[i] = int(input(f"Enter registration number last 3 digits of student {i+1}: "))
    marks[i] = int(input(f"Enter marks of student {i+1}: "))

print(f"\nMarks of each student in List: {marks}\n")

qualify_count = 0
fail_count = 0
print("Marks:")

for i in range(n):
    mark = marks[i]
    reg_no = reg_nos[i]

    if mark < 0 or mark > 100:
        print(mark, "→ Invalid")
    elif mark >= 90:
        qualify_count += 1
        print(mark, "→ Excellent")
    elif mark >= 75:
        qualify_count += 1
        print(mark, "→ Very Good")
    elif mark >= 60:
        qualify_count += 1
        print(mark, "→ Good")
    elif 35 <= mark < 40 and reg_no % 2 == 1:
        qualify_count += 1
        print(mark + 5, "→ Average (With extra grace marks)")
    elif mark >= 40:
        qualify_count += 1
        print(mark, "→ Average")
    else:
        qualify_count += 1
        fail_count += 1
        print(mark, "→ Fail")

print("\nFinal Summary:")
print("Total Valid Students:", qualify_count)
print("Total Failed Students:", fail_count)