# **Problem Statement:** Given n, print numbers from n down to 1 separated by spaces.

n = int(input())
# range(start, stop, steps): steps adds/deletes that much given steps
print(*range(n,0,-1)) # starts from 5 and each time deletes 1 from the n and stops at 0 , thus prints till 1