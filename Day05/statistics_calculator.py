# Statistics Calculator (Focus: Functions)

# Function to calculate mean
def calculate_mean(numbers):
    total = sum(numbers)
    return total / len(numbers)

# Function to calculate median
def calculate_median(numbers):
    numbers.sort()
    n = len(numbers)
    
    if n % 2 == 0:
        median = (numbers[n//2 - 1] + numbers[n//2]) / 2
    else:
        median = numbers[n//2]
    
    return median

# Function to calculate mode
def calculate_mode(numbers):
    freq = {}
    
    for num in numbers:
        freq[num] = freq.get(num, 0) + 1
    
    max_count = max(freq.values())
    
    mode = [key for key, value in freq.items() if value == max_count]
    
    return mode

# Input
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Function calls
mean = calculate_mean(numbers)
median = calculate_median(numbers)
mode = calculate_mode(numbers)

# Output
print("\n----- Statistics -----")
print("Numbers:", numbers)
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)