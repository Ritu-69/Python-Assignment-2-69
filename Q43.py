for i in range(1, 11):          # Outer loop for rows (1 to 10)
    for j in range(1, 11):      # Inner loop for columns (1 to 10)
        print(f"{i * j:4}", end="")
    print()                     # Move to the next line after each row
