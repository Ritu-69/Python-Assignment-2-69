# Number of rows in the pattern
rows = 5

# Outer loop handles the number of rows
for i in range(1, rows + 1):
    # Inner loop handles the number of stars in each row
    for j in range(i):
        print("*", end="")
    # Move to the next line after printing each row
    print()
