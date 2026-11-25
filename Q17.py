num = int(input("Enter a number: "))

# Check the least significant bit using bitwise AND
if num & 1:
    print(f"{num} is Odd")
else:
    print(f"{num} is Even")
