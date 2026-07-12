# **Problem Statement:** Given n, print the sum of all even numbers from 1 to n.

# **Input:** One integer n.

# **Output:** Sum of even numbers.

n = int(input())
total = 0
for i in range(2,n+1,2): #starts from 2 till n+1, skipps 2 steps 2 +2 = 4, 4 + 2 = 6, 6 + 2 = 8 .... like that 
    total = total + i
print(total)