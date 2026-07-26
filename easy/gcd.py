# **Problem Statement:** Given two integers, print their greatest common divisor.

# **Input:** Two integers a and b.

# **Output:** GCD of a and b.

a, b = map(int, input().split())
# a gets divided by b and in the next step a gets the value of b and b gets the remainder value of a % b
# eg, 
# a b
# 24 9
# 9 6
# 6 3
# 3 0
# as long as b becomes 0 the instant a is the gcd value
while b != 0:
    a , b = b, a%b
print(a)