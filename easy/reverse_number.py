# **Problem Statement:** Given a non-negative integer, print its digits in reverse order.
n  = input().strip()
# n[::-1] start, stop , steps -1 -> indicates 1 steps from the last
rev = n[::-1].lstrip("0")
print(rev if rev else "0")
