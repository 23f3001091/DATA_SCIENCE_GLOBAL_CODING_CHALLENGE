# Weekly Sales Analysis (Focus: Loops)

sales = []

# Input for 7 days
for i in range(7):
    amount = float(input(f"Enter sales for Day {i+1}: "))
    sales.append(amount)

# Calculate total using loop
total_sales = 0
for value in sales:
    total_sales += value

# Average
average_sales = total_sales / 7

# Output
print("\n----- Weekly Sales Report -----")
print("Daily Sales:", sales)
print("Total Sales:", total_sales)
print("Average Sales:", average_sales)