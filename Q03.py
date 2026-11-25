dividend = int(input("Enter the dividend: "))
divisor = int(input("Enter the divisor: "))

if divisor == 0:
    print("Error: Division by zero is not allowed.")
else:
    # Use integer division (//) to find the whole number quotient
    quotient = dividend // divisor
    remainder = dividend - (quotient * divisor)
    print(f"Remainder: {remainder}")
