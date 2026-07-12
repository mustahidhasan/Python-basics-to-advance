# **Problem Statement:** Given n, print n factorial. n! eg, 5! = 1 + 2 + 3 + 4 + 5
n = int(input())
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(factorial)
