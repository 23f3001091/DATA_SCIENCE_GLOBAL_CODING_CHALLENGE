# Student Marks Analysis (Mini Project)

# Dictionary to store student data
students = {}

n = int(input("Enter number of students: "))

# Input data
for i in range(n):
    name = input("\nEnter student name: ")
    marks = list(map(int, input("Enter marks (space separated): ").split()))
    students[name] = marks

# Analysis
print("\n===== Student Analysis =====")

for name, marks in students.items():
    total = sum(marks)
    average = total / len(marks)
    highest = max(marks)
    lowest = min(marks)

    print(f"\nStudent: {name}")
    print("Marks:", marks)
    print("Total:", total)
    print("Average:", average)
    print("Highest:", highest)
    print("Lowest:", lowest)

    # Result classification
    if average >= 40:
        print("Result: Pass")
    else:
        print("Result: Fail")