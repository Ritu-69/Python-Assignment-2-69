# Creating variables with lists
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

# Demonstrating 'is' operator
print("list1 is list2:", list1 is list2)   # False (different memory locations)
print("list1 is list3:", list1 is list3)   # True (same memory location)

# Demonstrating 'is not' operator
print("list1 is not list2:", list1 is not list2)   # True
print("list1 is not list3:", list1 is not list3)   # False
