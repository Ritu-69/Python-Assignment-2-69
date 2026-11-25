# Take two numbers as input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Compare the two numbers
if num1 > num2:
  print(f"{num1} is the greatest.")
elif num2 > num1:
  print(f"{num2} is the greatest.")
else:
  print("Both numbers are equal.")
