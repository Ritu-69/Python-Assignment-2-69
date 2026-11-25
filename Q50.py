rows = 5

# Outer loop controls the number of rows (5 down to 1)
for i in range(rows, 0, -1):
  # Inner loop prints stars equal to the current row number
  for j in range(i):
    print("*", end="")
  # Move to the next line after each row
  print()
