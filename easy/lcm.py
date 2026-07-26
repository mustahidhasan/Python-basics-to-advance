# **Problem Statement:** Given two integers, print their least common multiple.

# **Input:** Two integers a and b.

# **Output:** LCM of a and b.

# same as previous problem , we can use the gdc value here, just lcm = a * b/gcd(a, b)
a, b = map(int, input().split())
multiple = a * b
while b != 0:
    a, b = b, a % b
print(int(multiple/ a))