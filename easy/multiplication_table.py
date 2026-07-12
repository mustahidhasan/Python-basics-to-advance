# **Problem Statement:** Given n, print the multiplication table of n from 1 to 10.

# **Input:** One integer n.

# **Output:** 10 lines in the form n x i = result.
# Output:
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
# 3 x 4 = 12
# 3 x 5 = 15
# 3 x 6 = 18
# 3 x 7 = 21
# 3 x 8 = 24
# 3 x 9 = 27
# 3 x 10 = 30


n = int(input())
for i in range(1, 11):
    print(f'{n} x {i} = {n*i}')