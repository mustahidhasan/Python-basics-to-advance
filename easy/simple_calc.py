# **Problem Statement:** Given two integers and an operator +, -, *, or /, perform the operation. For division, print result with 2 digits after decimal.

# **Input:** Two integers a b and one operator op.

# **Output:** Calculated result.

a, b, op = input().split()
a = int(a)
b = int(b)

if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    div = a / b
    print(f'{div:.2f}')