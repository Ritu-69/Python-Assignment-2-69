# Define two integers
a = 10  # Binary: 1010
b = 4   # Binary: 0100

# Perform bitwise operations
bitwise_and = a & b
bitwise_or = a | b
bitwise_xor = a ^ b

# Display the results
print(f"a = {a} (Binary: {bin(a)[2:].zfill(4)})")
print(f"b = {b} (Binary: {bin(b)[2:].zfill(4)})\n")

print(f"Bitwise AND (a & b): {bitwise_and} (Binary: {bin(bitwise_and)[2:].zfill(4)})")
print(f"Bitwise OR  (a | b): {bitwise_or} (Binary: {bin(bitwise_or)[2:].zfill(4)})")
print(f"Bitwise XOR (a ^ b): {bitwise_xor} (Binary: {bin(bitwise_xor)[2:].zfill(4)})")
