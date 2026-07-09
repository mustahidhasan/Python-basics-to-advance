# print the larger integer amoong two input number

a, b = map(int, input().split())
print(a if a > b else b)