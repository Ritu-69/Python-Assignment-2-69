# Initialize a number
num = 10  # Binary: 1010

# Left-shift operator (<<)
# Shifts bits to the left by 2 positions (multiplies by 2^2 = 4)
left_shift = num << 2

# Right-shift operator (>>)
# Shifts bits to the right by 1 position (divides by 2^1 = 2)
right_shift = num >> 1

# Display results
print(f"Original number: {num} (Binary: {bin(num)})")
print(f"Left shift by 2 ({num} << 2): {left_shift} (Binary: {bin(left_shift)})")
print(f"Right shift by 1 ({num} >> 1): {right_shift} (Binary: {bin(right_shift)})")
