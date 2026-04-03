# Employee Salary Program (Focus: Variables)

# Input
employee_name = input("Enter employee name: ")
monthly_salary = float(input("Enter monthly salary: "))

# Calculations using variables
annual_salary = monthly_salary * 12
hra = monthly_salary * 0.20
bonus = monthly_salary * 0.10
gross_salary = monthly_salary + hra + bonus

# Simple tax logic
tax = annual_salary * 0.10

net_salary = annual_salary - tax

# Output
print("\n----- Salary Details -----")
print("Employee Name:", employee_name)
print("Monthly Salary:", monthly_salary)
print("Annual Salary:", annual_salary)
print("HRA:", hra)
print("Bonus:", bonus)
print("Gross Salary:", gross_salary)
print("Tax:", tax)
print("Net Salary:", net_salary)