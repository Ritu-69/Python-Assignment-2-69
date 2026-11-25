# Take a single character input from the user
char = input("Enter an alphabet: ")

# Check if the input is a single alphabetic character
if len(char) == 1 and char.isalpha():
    # Convert to lowercase to handle both uppercase and lowercase inputs
    if char.lower() in ('a', 'e', 'i', 'o', 'u'):
        print(f"'{char}' is a Vowel.")
    else:
        print(f"'{char}' is a Consonant.")
else:
    print("Invalid input. Please enter a single alphabet character.")
