num = int(input("Enter an integer: "))

# Handle negative numbers and zero
n = abs(num)
count = 0

if n == 0:
    count = 1
else:
    while n > 0:
        n //= 10  # Integer division removes the last digit
        count += 1

print("Number of digits:", count)
