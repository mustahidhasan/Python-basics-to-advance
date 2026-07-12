# **Problem Statement:** Given a non-negative integer, count how many digits it has.
n = int(input().strip()) # make is a complete string, no space or any extra things

# print(len(n))

def count_degits(n):
    count = 0
    if n == 1: count =1
    while n > 0:
        n = n // 10
        count += 1
    return count
print(count_degits(n))