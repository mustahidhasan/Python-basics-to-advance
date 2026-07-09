# 1. using map funciton a b gets the 2 input iteratively and doese the performation with a-b and a*b

# User Input
#    |
#    v
# "10 20"              input()
#    |
#    v
# ["10", "20"]         split()
#    |
#    v
# 10, 20               map(int, ...)
#    |
#    v
# a = 10
# b = 20               unpacking

a, b = (map(int, input().split()))
print(a-b)
print(a*b)