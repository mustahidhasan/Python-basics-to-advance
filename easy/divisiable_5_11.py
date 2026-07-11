# **Problem Statement:** Given an integer, check whether it is divisible by both 5 and 11.
n = int(input())
print("Yes" if n % 5 == 0 and n % 11 == 0 else "No")