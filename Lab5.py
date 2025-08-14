numbers = [5, 3, 8, 1, 9]

# Start with the first number in the list
min_value = numbers[0]

# Loop through each number in the list
for num in numbers:

# If the current number is smaller than min_value, update min_value
    if num < min_value:
        min_value = num

# Print the final result
print("Minimum value is:", min_value)