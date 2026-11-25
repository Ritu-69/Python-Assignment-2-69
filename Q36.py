num = int(input("Enter an integer: "))
reversed_num = 0

# Handle negative numbers by working with the absolute value
is_negative = num < 0
num = abs(num)

while num > 0:
    digit = num % 10                  # Extract the last digit
    reversed_num = reversed_num * 10 + digit  # Append digit to reversed_num
    num //= 10                        # Remove the last digit from num

if is_negative:
    reversed_num = -reversed_num

print("Reversed Number:", reversed_num)
