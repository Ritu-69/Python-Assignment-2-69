num = int(input("Enter a number: "))
total = 0

# Use abs() to handle negative numbers properly
temp = abs(num)

while temp > 0:
    digit = temp % 10      # Extract the last digit
    total += digit         # Add it to the sum
    temp //= 10            # Remove the last digit

print("Sum of digits:", total)
