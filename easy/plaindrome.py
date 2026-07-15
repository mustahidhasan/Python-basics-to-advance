# **Problem Statement:** Given a non-negative integer, check whether it reads the same backward.
n = input().strip()
print("Yes" if n == n[::-1] else "No") # if the number traversed value in backward 1 step ahead till start to stop is equal to actual number 