# Student Result Program with Grades

student_name = input("Enter student name: ")
marks = float(input("Enter marks: "))

if marks >= 75:
    result = "Distinction"
elif marks >= 60:
    result = "First Class"
elif marks >= 40:
    result = "Pass"
else:
    result = "Fail"

print("\n----- Result -----")
print("Student Name:", student_name)
print("Marks:", marks)
print("Result:", result)