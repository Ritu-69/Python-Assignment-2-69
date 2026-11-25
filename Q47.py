# Program to demonstrate the use of the pass statement inside a loop

for letter in "Python":
    if letter == "h":
        pass  # Placeholder: nothing happens here, execution continues normally
        print("This is a pass block")
    print("Current Letter:", letter)

print("Loop ended.")
