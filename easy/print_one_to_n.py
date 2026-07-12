#  Done Problem Statement: Given n, print numbers from 1 to n separated by spaces.

n = int(input()) # n = 5
# range(1, n + 1) : range(1,6)
print(*range(1, n+1)) # *range(1,6) = 1,2,3,4,5 unpacks that whole range and print indivisual thing