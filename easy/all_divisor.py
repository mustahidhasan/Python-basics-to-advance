# **Problem Statement:** Given n, print all positive divisors of n in increasing order.

# **Input:** One integer n.

n = int(input())
i = 1
while i < n+1:
    if n % i == 0:
        print(i, end=" ")
    i += 1
print()