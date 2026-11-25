# Input marks from the user
marks = float(input("Enter the student's marks (0-100): "))

# Determine grade using if-elif-else
if marks > 100 or marks < 0:
    print("Invalid marks! Please enter a value between 0 and 100.")
elif marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")
