import random

# Generate 5 random floating-point numbers between 0 and 10
numbers = [random.uniform(0, 10) for _ in range(5)]

# Display the numbers
print("Random numbers:")

for number in numbers:
    print(number)

# Find minimum and maximum
minimum = min(numbers)
maximum = max(numbers)

print("Minimum value:", minimum)
print("Maximum value:", maximum)