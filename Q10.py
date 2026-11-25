# Input a two-digit number
num = int(input("Enter a two-digit number: "))

# Extract the digits
tens = num // 10     # Integer division gets the first digit
ones = num % 10      # Modulus gets the last digit

# Calculate and display the sum
digit_sum = tens + ones
print("Sum of the digits:", digit_sum)
