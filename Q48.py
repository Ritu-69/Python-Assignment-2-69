numbers = [10, 20, 30, 40, 50]

# Case 1: Loop finishes normally (else block executes)
print("--- Searching for 60 ---")
for num in numbers:
  if num == 60:
    print("Found 60!")
    break
else:
  print("60 was not found in the list. (else block ran)")

# Case 2: Loop terminates early via break (else block is skipped)
print("\n--- Searching for 30 ---")
for num in numbers:
  if num == 30:
    print("Found 30! Stopping loop.")
    break
else:
  print("30 was not found in the list. (else block skipped)")
