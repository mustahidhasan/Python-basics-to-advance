# print the maxium among the 3 numbers

a, b, c = map(int, input().split())
if a > b and a > c:
    print(a)
else:
    print(b if b > c else c)