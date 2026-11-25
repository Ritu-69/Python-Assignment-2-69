# Program to demonstrate Python Operator Precedence

# 1. Parentheses () vs Multiplication * and Addition +
expr1 = 10 + 20 * 3
expr2 = (10 + 20) * 3
print(f"10 + 20 * 3   = {expr1}  (Multiplication before addition)")
print(f"(10 + 20) * 3 = {expr2}  (Parentheses evaluated first)\n")

# 2. Exponentiation ** vs Multiplication *
expr3 = 2 * 3 ** 2
print(f"2 * 3 ** 2    = {expr3}  (Exponentiation before multiplication)")

# Right-to-left associativity of Exponentiation **
expr4 = 2 ** 3 ** 2
print(f"2 ** 3 ** 2   = {expr4} (Evaluated right-to-left: 2 ** (3 ** 2) = 2 ** 9)\n")

# 3. Division /, Floor Division //, and Modulus % (Left-to-right associativity)
expr5 = 20 // 3 * 2
print(f"20 // 3 * 2   = {expr5}  (Evaluated left-to-right: (20 // 3) * 2)\n")

# 4. Arithmetic vs Comparison vs Logical Operators (not, and, or)
expr6 = 5 + 3 > 7 and not 4 == 5 or False
print(f"5 + 3 > 7 and not 4 == 5 or False = {expr6}")
