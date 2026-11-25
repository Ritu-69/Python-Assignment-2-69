num = int(input("Enter an integer: "))

# Use abs() to handle negative integers properly
last_digit = abs(num) % 10

print("Last digit:", last_digit)
