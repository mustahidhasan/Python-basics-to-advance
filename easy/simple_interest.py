p, r, t = map(float, input().split())
# simple interest logic is: principal amount * interest rate * time in years /100
si = p*t*r/100
print(f"{si:.2f}")