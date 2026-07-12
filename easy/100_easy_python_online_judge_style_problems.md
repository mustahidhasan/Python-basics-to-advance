These are original online-judge-style practice problems, not copied from any judge. Each includes a statement, sample tests, and a Python solution.

## 1. Sum of Two Numbers
- [x] Done
**Problem Statement:** Given two integers, print their sum.

**Input:** Two integers a and b.

**Output:** The sum of a and b.

**Sample Test Cases:**

Sample 1
```text
Input:
3 5

Output:
8
```

Sample 2
```text
Input:
-2 7

Output:
5
```

**Python Solution:**
```python
a, b = map(int, input().split())
print(a + b)
```

## 2. Difference and Product
- [x] Done
**Problem Statement:** Given two integers, print their difference and product on separate lines.

**Input:** Two integers a and b.

**Output:** First line: a - b. Second line: a * b.

**Sample Test Cases:**

Sample 1
```text
Input:
8 3

Output:
5
24
```

Sample 2
```text
Input:
4 10

Output:
-6
40
```

**Python Solution:**
```python
a, b = map(int, input().split())
print(a - b)
print(a * b)
```

## 3. Circle Area
- [x] Done
**Problem Statement:** Given the radius of a circle, print its area using pi = 3.1416. Print 2 digits after decimal.

**Input:** One float r.

**Output:** Area of the circle.

**Sample Test Cases:**

Sample 1
```text
Input:
2

Output:
12.57
```

Sample 2
```text
Input:
5

Output:
78.54
```

**Python Solution:**
```python
r = float(input())
area = 3.1416 * r * r
print(f"{area:.2f}")
```

## 4. Celsius to Fahrenheit
- [x] Done
**Problem Statement:** Given a temperature in Celsius, convert it to Fahrenheit.

**Input:** One float c.

**Output:** Fahrenheit value with 2 digits after decimal.

**Sample Test Cases:**

Sample 1
```text
Input:
0

Output:
32.00
```

Sample 2
```text
Input:
37

Output:
98.60
```

**Python Solution:**
```python
c = float(input())
f = c * 9 / 5 + 32
print(f"{f:.2f}")
```

## 5. Swap Two Numbers
- [x] Done
**Problem Statement:** Given two integers, print them after swapping their values.

**Input:** Two integers a and b.

**Output:** Print b and a.

**Sample Test Cases:**

Sample 1
```text
Input:
10 20

Output:
20 10
```

Sample 2
```text
Input:
5 -1

Output:
-1 5
```

**Python Solution:**
```python
a, b = map(int, input().split())
a, b = b, a
print(a, b)
```

## 6. Even or Odd
- [x] Done
**Problem Statement:** Given an integer, determine whether it is even or odd.

**Input:** One integer n.

**Output:** Print Even or Odd.

**Sample Test Cases:**

Sample 1
```text
Input:
4

Output:
Even
```

Sample 2
```text
Input:
7

Output:
Odd
```

**Python Solution:**
```python
n = int(input())
print("Even" if n % 2 == 0 else "Odd")
```

## 7. Positive Negative Zero
- [x] Done
**Problem Statement:** Given an integer, print whether it is Positive, Negative, or Zero.

**Input:** One integer n.

**Output:** Positive, Negative, or Zero.

**Sample Test Cases:**

Sample 1
```text
Input:
9

Output:
Positive
```

Sample 2
```text
Input:
0

Output:
Zero
```

Sample 3
```text
Input:
-3

Output:
Negative
```

**Python Solution:**
```python
n = int(input())
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")
```

## 8. Maximum of Two
- [x] Done
**Problem Statement:** Given two integers, print the larger one.

**Input:** Two integers a and b.

**Output:** The larger integer.

**Sample Test Cases:**

Sample 1
```text
Input:
7 3

Output:
7
```

Sample 2
```text
Input:
4 9

Output:
9
```

**Python Solution:**
```python
a, b = map(int, input().split())
print(max(a, b))
```
or 
``` python
a, b = map(int, input().split())
print(a if a > b else b)
```

## 9. Maximum of Three
- [ ] Done
**Problem Statement:** Given three integers, print the largest one.

**Input:** Three integers a, b, c.

**Output:** The largest integer.

**Sample Test Cases:**

Sample 1
```text
Input:
1 9 4

Output:
9
```

Sample 2
```text
Input:
-5 -2 -8

Output:
-2
```

**Python Solution:**
```python
a, b, c = map(int, input().split())
print(max(a, b, c))
```
or 
```python
a, b, c = map(int, input().split())
if a > b and a > c:
    print(a)
else:
    print(b if b > c else c)
```
## 10. Grade Calculator
- [x] Done
**Problem Statement:** Given marks from 0 to 100, print grade: A for 80+, B for 70+, C for 60+, D for 50+, otherwise F.

**Input:** One integer mark.

**Output:** Grade letter.

**Sample Test Cases:**

Sample 1
```text
Input:
85

Output:
A
```

Sample 2
```text
Input:
43

Output:
F
```

**Python Solution:**
```python
mark = int(input())
if mark >= 80:
    print("A")
elif mark >= 70:
    print("B")
elif mark >= 60:
    print("C")
elif mark >= 50:
    print("D")
else:
    print("F")
```

## 11. Leap Year
- [x] Done
**Problem Statement:** Given a year, determine if it is a leap year. A year is leap if divisible by 400 or divisible by 4 but not by 100.

**Input:** One integer year.

**Output:** Leap Year or Not Leap Year.

**Sample Test Cases:**

Sample 1
```text
Input:
2024

Output:
Leap Year
```

Sample 2
```text
Input:
1900

Output:
Not Leap Year
```

**Python Solution:**
```python
year = int(input())
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not Leap Year")
```

## 12. Last Digit
- [x] Done
**Problem Statement:** Given a non-negative integer, print its last digit.

**Input:** One integer n.

**Output:** Last digit of n.

**Sample Test Cases:**

Sample 1
```text
Input:
12345

Output:
5
```

Sample 2
```text
Input:
90

Output:
0
```

**Python Solution:**
```python
n = int(input())
print(n % 10)
```

## 13. Digit Sum Two
- [x] Done
**Problem Statement:** Given a two-digit number, print the sum of its digits.

**Input:** One two-digit integer n.

**Output:** Sum of digits.

**Sample Test Cases:**

Sample 1
```text
Input:
57

Output:
12
```

Sample 2
```text
Input:
10

Output:
1
```

**Python Solution:**
```python
n = int(input())
print(n // 10 + n % 10)
```

## 14. Simple Interest
- [x] Done
**Problem Statement:** Given principal, rate, and time, calculate simple interest: P*R*T/100.

**Input:** Three floats p, r, t.

**Output:** Simple interest with 2 digits after decimal.

**Sample Test Cases:**

Sample 1
```text
Input:
1000 5 2

Output:
100.00
```

Sample 2
```text
Input:
500 10 1

Output:
50.00
```

**Python Solution:**
```python
p, r, t = map(float, input().split())
si = p * r * t / 100
print(f"{si:.2f}")
```

## 15. Rectangle Area Perimeter
- [x] Done
**Problem Statement:** Given length and width of a rectangle, print area and perimeter.

**Input:** Two integers l and w.

**Output:** Area and perimeter separated by space.

**Sample Test Cases:**

Sample 1
```text
Input:
5 3

Output:
15 16
```

Sample 2
```text
Input:
10 2

Output:
20 24
```

**Python Solution:**
```python
l, w = map(int, input().split())
area = l * w
perimeter = 2 * (l + w)
print(area, perimeter)
```

## 16. Absolute Value
- [x] Done
**Problem Statement:** Given an integer, print its absolute value.

**Input:** One integer n.

**Output:** Absolute value of n.

**Sample Test Cases:**

Sample 1
```text
Input:
-9

Output:
9
```

Sample 2
```text
Input:
12

Output:
12
```

**Python Solution:**
```python
n = int(input())
print(abs(n))
```
or 
```python
n = int(input())
print(n if n >= 0 else -(n))
```

## 17. Voting Eligibility
- [x] Done
**Problem Statement:** Given age, print Eligible if age is at least 18, otherwise Not Eligible.

**Input:** One integer age.

**Output:** Eligible or Not Eligible.

**Sample Test Cases:**

Sample 1
```text
Input:
20

Output:
Eligible
```

Sample 2
```text
Input:
16

Output:
Not Eligible
```

**Python Solution:**
```python
age = int(input())
print("Eligible" if age >= 18 else "Not Eligible")
```

## 18. Divisible by 5 and 11
- [x] Done
**Problem Statement:** Given an integer, check whether it is divisible by both 5 and 11.

**Input:** One integer n.

**Output:** Yes or No.

**Sample Test Cases:**

Sample 1
```text
Input:
55

Output:
Yes
```

Sample 2
```text
Input:
25

Output:
No
```

**Python Solution:**
```python
n = int(input())
print("Yes" if n % 5 == 0 and n % 11 == 0 else "No")
```

## 19. Character Type
- [x] Done
**Problem Statement:** Given a single English letter, print Vowel if it is a vowel, otherwise Consonant.

**Input:** One character ch.

**Output:** Vowel or Consonant.

**Sample Test Cases:**

Sample 1
```text
Input:
a

Output:
Vowel
```

Sample 2
```text
Input:
Z

Output:
Consonant
```

**Python Solution:**
```python
ch = input().strip().lower()
print("Vowel" if ch in "aeiou" else "Consonant")
print("Vowel" if ch in "aeiou" or ch in "AEIOU" else "Consonant") # better
```

## 20. Simple Calculator
- [ ] Done
**Problem Statement:** Given two integers and an operator +, -, *, or /, perform the operation. For division, print result with 2 digits after decimal.

**Input:** Two integers a b and one operator op.

**Output:** Calculated result.

**Sample Test Cases:**

Sample 1
```text
Input:
10 3 +

Output:
13
```

Sample 2
```text
Input:
10 4 /

Output:
2.50
```

**Python Solution:**
```python
a, b, op = input().split()
a = int(a)
b = int(b)

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(f"{a / b:.2f}")
```

## 21. Print 1 to N
- [x] Done
**Problem Statement:** Given n, print numbers from 1 to n separated by spaces.

**Input:** One integer n.

**Output:** Numbers from 1 to n.

**Sample Test Cases:**

Sample 1
```text
Input:
5

Output:
1 2 3 4 5
```

Sample 2
```text
Input:
1

Output:
1
```

**Python Solution:**
```python
n = int(input())
print(*range(1, n + 1))
```

## 22. Print N to 1
- [x] Done
**Problem Statement:** Given n, print numbers from n down to 1 separated by spaces.

**Input:** One integer n.

**Output:** Numbers from n to 1.

**Sample Test Cases:**

Sample 1
```text
Input:
5

Output:
5 4 3 2 1
```

Sample 2
```text
Input:
2

Output:
2 1
```

**Python Solution:**
```python
n = int(input())
print(*range(n, 0, -1))
```

## 23. Sum 1 to N
- [x] Done
**Problem Statement:** Given n, print the sum of integers from 1 to n.

**Input:** One integer n.

**Output:** Sum from 1 to n.

**Sample Test Cases:**

Sample 1
```text
Input:
5

Output:
15
```

Sample 2
```text
Input:
10

Output:
55
```

**Python Solution:**
```python
n = int(input())
print(n * (n + 1) // 2)
```

## 24. Sum of Even Numbers
- [x] Done
**Problem Statement:** Given n, print the sum of all even numbers from 1 to n.

**Input:** One integer n.

**Output:** Sum of even numbers.

**Sample Test Cases:**

Sample 1
```text
Input:
10

Output:
30
```

Sample 2
```text
Input:
5

Output:
6
```

**Python Solution:**
```python
n = int(input())
total = 0
for i in range(2, n + 1, 2):
    total += i
print(total)
```

## 25. Factorial
- [x] Done
**Problem Statement:** Given n, print n factorial.

**Input:** One integer n.

**Output:** n!.

**Sample Test Cases:**

Sample 1
```text
Input:
5

Output:
120
```

Sample 2
```text
Input:
0

Output:
1
```

**Python Solution:**
```python
n = int(input())
ans = 1
for i in range(1, n + 1):
    ans *= i
print(ans)
```

## 26. Multiplication Table
- [x] Done
**Problem Statement:** Given n, print the multiplication table of n from 1 to 10.

**Input:** One integer n.

**Output:** 10 lines in the form n x i = result.

**Sample Test Cases:**

Sample 1
```text
Input:
3

Output:
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30
```

**Python Solution:**
```python
n = int(input())
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
```

## 27. Count Digits
- [ ] Done
**Problem Statement:** Given a non-negative integer, count how many digits it has.

**Input:** One integer n.

**Output:** Number of digits.

**Sample Test Cases:**

Sample 1
```text
Input:
12345

Output:
5
```

Sample 2
```text
Input:
0

Output:
1
```

**Python Solution:**
```python
n = input().strip()
print(len(n))
```

## 28. Sum of Digits
- [ ] Done
**Problem Statement:** Given a non-negative integer, print the sum of its digits.

**Input:** One integer n.

**Output:** Sum of digits.

**Sample Test Cases:**

Sample 1
```text
Input:
1234

Output:
10
```

Sample 2
```text
Input:
900

Output:
9
```

**Python Solution:**
```python
s = input().strip()
print(sum(int(ch) for ch in s))
```

## 29. Reverse Number
- [ ] Done
**Problem Statement:** Given a non-negative integer, print its digits in reverse order.

**Input:** One integer n.

**Output:** Reversed number without leading zeros.

**Sample Test Cases:**

Sample 1
```text
Input:
1230

Output:
321
```

Sample 2
```text
Input:
500

Output:
5
```

**Python Solution:**
```python
s = input().strip()
rev = s[::-1].lstrip("0")
print(rev if rev else "0")
```

## 30. Palindrome Number
- [ ] Done
**Problem Statement:** Given a non-negative integer, check whether it reads the same backward.

**Input:** One integer n.

**Output:** Yes or No.

**Sample Test Cases:**

Sample 1
```text
Input:
121

Output:
Yes
```

Sample 2
```text
Input:
123

Output:
No
```

**Python Solution:**
```python
s = input().strip()
print("Yes" if s == s[::-1] else "No")
```

## 31. Power
- [ ] Done
**Problem Statement:** Given integers a and b, print a raised to the power b.

**Input:** Two integers a and b.

**Output:** a^b.

**Sample Test Cases:**

Sample 1
```text
Input:
2 5

Output:
32
```

Sample 2
```text
Input:
3 3

Output:
27
```

**Python Solution:**
```python
a, b = map(int, input().split())
print(a ** b)
```

## 32. Prime Check
- [ ] Done
**Problem Statement:** Given n, determine whether it is prime.

**Input:** One integer n.

**Output:** Prime or Not Prime.

**Sample Test Cases:**

Sample 1
```text
Input:
7

Output:
Prime
```

Sample 2
```text
Input:
12

Output:
Not Prime
```

**Python Solution:**
```python
n = int(input())

if n < 2:
    print("Not Prime")
else:
    prime = True
    i = 2
    while i * i <= n:
        if n % i == 0:
            prime = False
            break
        i += 1
    print("Prime" if prime else "Not Prime")
```

## 33. All Divisors
- [ ] Done
**Problem Statement:** Given n, print all positive divisors of n in increasing order.

**Input:** One integer n.

**Output:** Divisors separated by spaces.

**Sample Test Cases:**

Sample 1
```text
Input:
12

Output:
1 2 3 4 6 12
```

Sample 2
```text
Input:
7

Output:
1 7
```

**Python Solution:**
```python
n = int(input())
ans = []
for i in range(1, n + 1):
    if n % i == 0:
        ans.append(i)
print(*ans)
```

## 34. GCD
- [ ] Done
**Problem Statement:** Given two integers, print their greatest common divisor.

**Input:** Two integers a and b.

**Output:** GCD of a and b.

**Sample Test Cases:**

Sample 1
```text
Input:
12 18

Output:
6
```

Sample 2
```text
Input:
7 5

Output:
1
```

**Python Solution:**
```python
import math

a, b = map(int, input().split())
print(math.gcd(a, b))
```

## 35. LCM
- [ ] Done
**Problem Statement:** Given two integers, print their least common multiple.

**Input:** Two integers a and b.

**Output:** LCM of a and b.

**Sample Test Cases:**

Sample 1
```text
Input:
4 6

Output:
12
```

Sample 2
```text
Input:
5 7

Output:
35
```

**Python Solution:**
```python
import math

a, b = map(int, input().split())
print(a * b // math.gcd(a, b))
```

## 36. Fibonacci Nth
- [ ] Done
**Problem Statement:** Given n, print the nth Fibonacci number where F0=0 and F1=1.

**Input:** One integer n.

**Output:** nth Fibonacci number.

**Sample Test Cases:**

Sample 1
```text
Input:
0

Output:
0
```

Sample 2
```text
Input:
7

Output:
13
```

**Python Solution:**
```python
n = int(input())
a, b = 0, 1
for _ in range(n):
    a, b = b, a + b
print(a)
```

## 37. Fibonacci Series
- [ ] Done
**Problem Statement:** Given n, print first n Fibonacci numbers.

**Input:** One integer n.

**Output:** First n Fibonacci numbers.

**Sample Test Cases:**

Sample 1
```text
Input:
6

Output:
0 1 1 2 3 5
```

Sample 2
```text
Input:
1

Output:
0
```

**Python Solution:**
```python
n = int(input())
ans = []
a, b = 0, 1
for _ in range(n):
    ans.append(a)
    a, b = b, a + b
print(*ans)
```

## 38. Armstrong Number
- [ ] Done
**Problem Statement:** Given a number n, check whether it is an Armstrong number. Sum of each digit raised to number of digits should equal n.

**Input:** One integer n.

**Output:** Yes or No.

**Sample Test Cases:**

Sample 1
```text
Input:
153

Output:
Yes
```

Sample 2
```text
Input:
123

Output:
No
```

**Python Solution:**
```python
s = input().strip()
power = len(s)
total = sum(int(ch) ** power for ch in s)
print("Yes" if total == int(s) else "No")
```

## 39. Perfect Number
- [ ] Done
**Problem Statement:** Given n, check whether the sum of proper divisors of n equals n.

**Input:** One integer n.

**Output:** Yes or No.

**Sample Test Cases:**

Sample 1
```text
Input:
6

Output:
Yes
```

Sample 2
```text
Input:
10

Output:
No
```

**Python Solution:**
```python
n = int(input())
if n <= 1:
    print("No")
else:
    total = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    print("Yes" if total == n else "No")
```

## 40. Number of Factors
- [ ] Done
**Problem Statement:** Given n, print how many positive factors it has.

**Input:** One integer n.

**Output:** Number of factors.

**Sample Test Cases:**

Sample 1
```text
Input:
12

Output:
6
```

Sample 2
```text
Input:
7

Output:
2
```

**Python Solution:**
```python
n = int(input())
count = 0
for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        count += 1
        if i != n // i:
            count += 1
print(count)
```

## 41. Sum of Squares
- [ ] Done
**Problem Statement:** Given n, print 1^2 + 2^2 + ... + n^2.

**Input:** One integer n.

**Output:** Sum of squares.

**Sample Test Cases:**

Sample 1
```text
Input:
3

Output:
14
```

Sample 2
```text
Input:
5

Output:
55
```

**Python Solution:**
```python
n = int(input())
print(n * (n + 1) * (2 * n + 1) // 6)
```

## 42. Odd Numbers in Range
- [ ] Done
**Problem Statement:** Given a and b, print all odd numbers between a and b inclusive.

**Input:** Two integers a and b.

**Output:** Odd numbers separated by spaces. Print Empty if none.

**Sample Test Cases:**

Sample 1
```text
Input:
3 9

Output:
3 5 7 9
```

Sample 2
```text
Input:
2 2

Output:
Empty
```

**Python Solution:**
```python
a, b = map(int, input().split())
ans = [x for x in range(a, b + 1) if x % 2 != 0]
print(*ans if ans else ["Empty"])
```

## 43. Count Multiples
- [ ] Done
**Problem Statement:** Given n and k, count numbers from 1 to n divisible by k.

**Input:** Two integers n and k.

**Output:** Count of multiples.

**Sample Test Cases:**

Sample 1
```text
Input:
10 2

Output:
5
```

Sample 2
```text
Input:
20 6

Output:
3
```

**Python Solution:**
```python
n, k = map(int, input().split())
print(n // k)
```

## 44. Average of N Numbers
- [ ] Done
**Problem Statement:** Given n numbers, print their average with 2 digits after decimal.

**Input:** First line n. Second line n integers.

**Output:** Average value.

**Sample Test Cases:**

Sample 1
```text
Input:
5
1 2 3 4 5

Output:
3.00
```

Sample 2
```text
Input:
3
10 20 30

Output:
20.00
```

**Python Solution:**
```python
n = int(input())
arr = list(map(int, input().split()))
print(f"{sum(arr) / n:.2f}")
```

## 45. Minimum Coins
- [ ] Done
**Problem Statement:** Given an amount n, find the minimum number of coins using denominations 100, 50, 20, 10, 5, 2, 1.

**Input:** One integer n.

**Output:** Minimum number of coins.

**Sample Test Cases:**

Sample 1
```text
Input:
188

Output:
6
```

Sample 2
```text
Input:
7

Output:
2
```

**Python Solution:**
```python
n = int(input())
coins = [100, 50, 20, 10, 5, 2, 1]
count = 0
for coin in coins:
    count += n // coin
    n %= coin
print(count)
```

## 46. Array Sum
- [ ] Done
**Problem Statement:** Given an array of n integers, print the sum of all elements.

**Input:** First line n. Second line n integers.

**Output:** Sum of array.

**Sample Test Cases:**

Sample 1
```text
Input:
5
1 2 3 4 5

Output:
15
```

Sample 2
```text
Input:
3
-1 2 5

Output:
6
```

**Python Solution:**
```python
n = int(input())
arr = list(map(int, input().split()))
print(sum(arr))
```

## 47. Array Maximum
- [ ] Done
**Problem Statement:** Given an array of n integers, print the maximum element.

**Input:** First line n. Second line n integers.

**Output:** Maximum element.

**Sample Test Cases:**

Sample 1
```text
Input:
5
1 9 2 8 3

Output:
9
```

Sample 2
```text
Input:
3
-5 -2 -9

Output:
-2
```

**Python Solution:**
```python
n = int(input())
arr = list(map(int, input().split()))
print(max(arr))
```

## 48. Array Minimum
- [ ] Done
**Problem Statement:** Given an array of n integers, print the minimum element.

**Input:** First line n. Second line n integers.

**Output:** Minimum element.

**Sample Test Cases:**

Sample 1
```text
Input:
5
1 9 2 8 3

Output:
1
```

Sample 2
```text
Input:
3
-5 -2 -9

Output:
-9
```

**Python Solution:**
```python
n = int(input())
arr = list(map(int, input().split()))
print(min(arr))
```

## 49. Count Even Odd
- [ ] Done
**Problem Statement:** Given an array, count even and odd numbers.

**Input:** First line n. Second line n integers.

**Output:** Even count and odd count.

**Sample Test Cases:**

Sample 1
```text
Input:
5
1 2 3 4 5

Output:
2 3
```

Sample 2
```text
Input:
4
2 4 6 8

Output:
4 0
```

**Python Solution:**
```python
n = int(input())
arr = list(map(int, input().split()))
even = sum(1 for x in arr if x % 2 == 0)
odd = n - even
print(even, odd)
```

## 50. Search Element
- [ ] Done
**Problem Statement:** Given an array and a target x, print Found if x exists, otherwise Not Found.

**Input:** First line n. Second line n integers. Third line x.

**Output:** Found or Not Found.

**Sample Test Cases:**

Sample 1
```text
Input:
5
1 2 3 4 5
3

Output:
Found
```

Sample 2
```text
Input:
4
7 8 9 10
6

Output:
Not Found
```

**Python Solution:**
```python
n = int(input())
arr = list(map(int, input().split()))
x = int(input())
print("Found" if x in arr else "Not Found")
```

## 51. First Position
- [ ] Done
**Problem Statement:** Given an array and target x, print the first 1-based position of x. If not found, print -1.

**Input:** First line n. Second line n integers. Third line x.

**Output:** First position or -1.

**Sample Test Cases:**

Sample 1
```text
Input:
5
4 2 7 2 9
2

Output:
2
```

Sample 2
```text
Input:
3
1 2 3
5

Output:
-1
```

**Python Solution:**
```python
n = int(input())
arr = list(map(int, input().split()))
x = int(input())

pos = -1
for i, value in enumerate(arr):
    if value == x:
        pos = i + 1
        break
print(pos)
```

## 52. Reverse Array
- [ ] Done
**Problem Statement:** Given an array, print it in reverse order.

**Input:** First line n. Second line n integers.

**Output:** Reversed array.

**Sample Test Cases:**

Sample 1
```text
Input:
5
1 2 3 4 5

Output:
5 4 3 2 1
```

Sample 2
```text
Input:
3
9 8 7

Output:
7 8 9
```

**Python Solution:**
```python
n = int(input())
arr = list(map(int, input().split()))
print(*arr[::-1])
```

## 53. Sort Ascending
- [ ] Done
**Problem Statement:** Given an array, print it sorted in ascending order.

**Input:** First line n. Second line n integers.

**Output:** Sorted array.

**Sample Test Cases:**

Sample 1
```text
Input:
5
4 1 3 2 5

Output:
1 2 3 4 5
```

Sample 2
```text
Input:
3
9 -1 0

Output:
-1 0 9
```

**Python Solution:**
```python
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
print(*arr)
```

## 54. Sort Descending
- [ ] Done
**Problem Statement:** Given an array, print it sorted in descending order.

**Input:** First line n. Second line n integers.

**Output:** Sorted array descending.

**Sample Test Cases:**

Sample 1
```text
Input:
5
4 1 3 2 5

Output:
5 4 3 2 1
```

Sample 2
```text
Input:
3
9 -1 0

Output:
9 0 -1
```

**Python Solution:**
```python
n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
print(*arr)
```

## 55. Second Largest
- [ ] Done
**Problem Statement:** Given an array, print the second largest distinct value. If it does not exist, print None.

**Input:** First line n. Second line n integers.

**Output:** Second largest distinct value or None.

**Sample Test Cases:**

Sample 1
```text
Input:
5
1 5 3 5 2

Output:
3
```

Sample 2
```text
Input:
3
7 7 7

Output:
None
```

**Python Solution:**
```python
n = int(input())
arr = list(map(int, input().split()))
unique = sorted(set(arr), reverse=True)
print(unique[1] if len(unique) >= 2 else "None")
```

## 56. Remove Duplicates
- [ ] Done
**Problem Statement:** Given an array, print elements after removing duplicates while keeping first occurrence order.

**Input:** First line n. Second line n integers.

**Output:** Array without duplicates.

**Sample Test Cases:**

Sample 1
```text
Input:
7
1 2 1 3 2 4 3

Output:
1 2 3 4
```

Sample 2
```text
Input:
4
5 5 5 5

Output:
5
```

**Python Solution:**
```python
n = int(input())
arr = list(map(int, input().split()))
seen = set()
ans = []
for x in arr:
    if x not in seen:
        seen.add(x)
        ans.append(x)
print(*ans)
```

## 57. Frequency Count
- [ ] Done
**Problem Statement:** Given an array and a number x, count how many times x appears.

**Input:** First line n. Second line n integers. Third line x.

**Output:** Frequency of x.

**Sample Test Cases:**

Sample 1
```text
Input:
6
1 2 2 3 2 4
2

Output:
3
```

Sample 2
```text
Input:
3
5 6 7
8

Output:
0
```

**Python Solution:**
```python
n = int(input())
arr = list(map(int, input().split()))
x = int(input())
print(arr.count(x))
```

## 58. Positive Negative Count
- [ ] Done
**Problem Statement:** Given an array, count positive, negative, and zero values.

**Input:** First line n. Second line n integers.

**Output:** Positive count, negative count, zero count.

**Sample Test Cases:**

Sample 1
```text
Input:
6
1 -2 0 5 -1 0

Output:
2 2 2
```

Sample 2
```text
Input:
3
0 0 1

Output:
1 0 2
```

**Python Solution:**
```python
n = int(input())
arr = list(map(int, input().split()))
pos = neg = zero = 0
for x in arr:
    if x > 0:
        pos += 1
    elif x < 0:
        neg += 1
    else:
        zero += 1
print(pos, neg, zero)
```

## 59. Pair Sum
- [ ] Done
**Problem Statement:** Given an array and target k, determine whether any two different elements sum to k.

**Input:** First line n. Second line n integers. Third line k.

**Output:** Yes or No.

**Sample Test Cases:**

Sample 1
```text
Input:
5
1 2 3 4 5
9

Output:
Yes
```

Sample 2
```text
Input:
4
1 2 3 4
8

Output:
No
```

**Python Solution:**
```python
n = int(input())
arr = list(map(int, input().split()))
k = int(input())

seen = set()
ok = False
for x in arr:
    if k - x in seen:
        ok = True
        break
    seen.add(x)

print("Yes" if ok else "No")
```

## 60. Prefix Sum Queries
- [ ] Done
**Problem Statement:** Given an array and q queries, each query l r asks for sum from l to r using 1-based indexing.

**Input:** First line n. Second line n integers. Third line q. Next q lines contain l r.

**Output:** For each query, print range sum.

**Sample Test Cases:**

Sample 1
```text
Input:
5
1 2 3 4 5
2
1 3
2 5

Output:
6
14
```

**Python Solution:**
```python
n = int(input())
arr = list(map(int, input().split()))
prefix = [0]
for x in arr:
    prefix.append(prefix[-1] + x)

q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    print(prefix[r] - prefix[l - 1])
```

## 61. Rotate Right Once
- [ ] Done
**Problem Statement:** Given an array, rotate it right by one position.

**Input:** First line n. Second line n integers.

**Output:** Rotated array.

**Sample Test Cases:**

Sample 1
```text
Input:
5
1 2 3 4 5

Output:
5 1 2 3 4
```

Sample 2
```text
Input:
1
9

Output:
9
```

**Python Solution:**
```python
n = int(input())
arr = list(map(int, input().split()))
if n > 0:
    arr = [arr[-1]] + arr[:-1]
print(*arr)
```

## 62. Rotate Left K
- [ ] Done
**Problem Statement:** Given an array and k, rotate the array left by k positions.

**Input:** First line n. Second line n integers. Third line k.

**Output:** Rotated array.

**Sample Test Cases:**

Sample 1
```text
Input:
5
1 2 3 4 5
2

Output:
3 4 5 1 2
```

Sample 2
```text
Input:
4
10 20 30 40
5

Output:
20 30 40 10
```

**Python Solution:**
```python
n = int(input())
arr = list(map(int, input().split()))
k = int(input()) % n
arr = arr[k:] + arr[:k]
print(*arr)
```

## 63. Merge Two Arrays
- [ ] Done
**Problem Statement:** Given two arrays, merge them and print the result.

**Input:** First line n. Second line n integers. Third line m. Fourth line m integers.

**Output:** Merged array.

**Sample Test Cases:**

Sample 1
```text
Input:
3
1 2 3
2
4 5

Output:
1 2 3 4 5
```

Sample 2
```text
Input:
2
9 8
3
7 6 5

Output:
9 8 7 6 5
```

**Python Solution:**
```python
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
print(*(a + b))
```

## 64. Intersection Unique
- [ ] Done
**Problem Statement:** Given two arrays, print common distinct elements in increasing order. If none, print Empty.

**Input:** First line n. Second line n integers. Third line m. Fourth line m integers.

**Output:** Common unique elements.

**Sample Test Cases:**

Sample 1
```text
Input:
5
1 2 3 4 5
4
3 4 4 7

Output:
3 4
```

Sample 2
```text
Input:
3
1 2 3
2
8 9

Output:
Empty
```

**Python Solution:**
```python
n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = set(map(int, input().split()))

ans = sorted(a & b)
print(*ans if ans else ["Empty"])
```

## 65. Missing Number
- [ ] Done
**Problem Statement:** Numbers from 1 to n are given with one number missing. Find the missing number.

**Input:** First line n. Second line n-1 integers.

**Output:** Missing number.

**Sample Test Cases:**

Sample 1
```text
Input:
5
1 2 4 5

Output:
3
```

Sample 2
```text
Input:
3
2 3

Output:
1
```

**Python Solution:**
```python
n = int(input())
arr = list(map(int, input().split()))
expected = n * (n + 1) // 2
print(expected - sum(arr))
```

## 66. Maximum Subarray Easy
- [ ] Done
**Problem Statement:** Given an array, find the maximum sum of any non-empty contiguous subarray.

**Input:** First line n. Second line n integers.

**Output:** Maximum subarray sum.

**Sample Test Cases:**

Sample 1
```text
Input:
5
-2 1 -3 4 -1

Output:
4
```

Sample 2
```text
Input:
4
1 2 3 4

Output:
10
```

**Python Solution:**
```python
n = int(input())
arr = list(map(int, input().split()))

best = current = arr[0]
for x in arr[1:]:
    current = max(x, current + x)
    best = max(best, current)

print(best)
```

## 67. Count Greater Than X
- [ ] Done
**Problem Statement:** Given an array and x, count how many elements are greater than x.

**Input:** First line n. Second line n integers. Third line x.

**Output:** Count.

**Sample Test Cases:**

Sample 1
```text
Input:
5
1 5 7 2 9
5

Output:
2
```

Sample 2
```text
Input:
3
1 2 3
10

Output:
0
```

**Python Solution:**
```python
n = int(input())
arr = list(map(int, input().split()))
x = int(input())
print(sum(1 for v in arr if v > x))
```

## 68. Replace Negative With Zero
- [ ] Done
**Problem Statement:** Given an array, replace every negative number with 0 and print the array.

**Input:** First line n. Second line n integers.

**Output:** Modified array.

**Sample Test Cases:**

Sample 1
```text
Input:
5
1 -2 3 -4 5

Output:
1 0 3 0 5
```

Sample 2
```text
Input:
3
-1 -2 -3

Output:
0 0 0
```

**Python Solution:**
```python
n = int(input())
arr = list(map(int, input().split()))
arr = [0 if x < 0 else x for x in arr]
print(*arr)
```

## 69. Array Is Sorted
- [ ] Done
**Problem Statement:** Given an array, check whether it is sorted in non-decreasing order.

**Input:** First line n. Second line n integers.

**Output:** Yes or No.

**Sample Test Cases:**

Sample 1
```text
Input:
5
1 2 2 4 5

Output:
Yes
```

Sample 2
```text
Input:
4
1 3 2 4

Output:
No
```

**Python Solution:**
```python
n = int(input())
arr = list(map(int, input().split()))
print("Yes" if arr == sorted(arr) else "No")
```

## 70. Move Zeros End
- [ ] Done
**Problem Statement:** Given an array, move all zeros to the end while keeping order of non-zero elements.

**Input:** First line n. Second line n integers.

**Output:** Modified array.

**Sample Test Cases:**

Sample 1
```text
Input:
6
0 1 0 3 12 0

Output:
1 3 12 0 0 0
```

Sample 2
```text
Input:
3
0 0 1

Output:
1 0 0
```

**Python Solution:**
```python
n = int(input())
arr = list(map(int, input().split()))
non_zero = [x for x in arr if x != 0]
zeros = [0] * (n - len(non_zero))
print(*(non_zero + zeros))
```

## 71. String Length
- [ ] Done
**Problem Statement:** Given a string, print its length.

**Input:** One line string s.

**Output:** Length of s.

**Sample Test Cases:**

Sample 1
```text
Input:
hello

Output:
5
```

Sample 2
```text
Input:
Python 3

Output:
8
```

**Python Solution:**
```python
s = input()
print(len(s))
```

## 72. Reverse String
- [ ] Done
**Problem Statement:** Given a string, print it in reverse.

**Input:** One line string s.

**Output:** Reversed string.

**Sample Test Cases:**

Sample 1
```text
Input:
hello

Output:
olleh
```

Sample 2
```text
Input:
abc

Output:
cba
```

**Python Solution:**
```python
s = input()
print(s[::-1])
```

## 73. Palindrome String
- [ ] Done
**Problem Statement:** Given a string, check whether it is a palindrome.

**Input:** One line string s.

**Output:** Yes or No.

**Sample Test Cases:**

Sample 1
```text
Input:
madam

Output:
Yes
```

Sample 2
```text
Input:
hello

Output:
No
```

**Python Solution:**
```python
s = input().strip()
print("Yes" if s == s[::-1] else "No")
```

## 74. Count Vowels
- [ ] Done
**Problem Statement:** Given a string, count vowels a, e, i, o, u. Ignore case.

**Input:** One line string s.

**Output:** Number of vowels.

**Sample Test Cases:**

Sample 1
```text
Input:
Education

Output:
5
```

Sample 2
```text
Input:
sky

Output:
0
```

**Python Solution:**
```python
s = input().lower()
count = sum(1 for ch in s if ch in "aeiou")
print(count)
```

## 75. Count Words
- [ ] Done
**Problem Statement:** Given a sentence, count how many words it contains.

**Input:** One line sentence.

**Output:** Number of words.

**Sample Test Cases:**

Sample 1
```text
Input:
I love Python

Output:
3
```

Sample 2
```text
Input:
hello

Output:
1
```

**Python Solution:**
```python
s = input().strip()
print(0 if s == "" else len(s.split()))
```

## 76. Uppercase String
- [ ] Done
**Problem Statement:** Given a string, convert it to uppercase.

**Input:** One line string s.

**Output:** Uppercase string.

**Sample Test Cases:**

Sample 1
```text
Input:
hello

Output:
HELLO
```

Sample 2
```text
Input:
PyThOn

Output:
PYTHON
```

**Python Solution:**
```python
s = input()
print(s.upper())
```

## 77. Lowercase String
- [ ] Done
**Problem Statement:** Given a string, convert it to lowercase.

**Input:** One line string s.

**Output:** Lowercase string.

**Sample Test Cases:**

Sample 1
```text
Input:
HELLO

Output:
hello
```

Sample 2
```text
Input:
PyThOn

Output:
python
```

**Python Solution:**
```python
s = input()
print(s.lower())
```

## 78. Count Character
- [ ] Done
**Problem Statement:** Given a string and a character, count how many times the character appears.

**Input:** First line string s. Second line character ch.

**Output:** Frequency of ch.

**Sample Test Cases:**

Sample 1
```text
Input:
banana
a

Output:
3
```

Sample 2
```text
Input:
Hello
l

Output:
2
```

**Python Solution:**
```python
s = input()
ch = input()
print(s.count(ch))
```

## 79. Remove Spaces
- [ ] Done
**Problem Statement:** Given a string, remove all spaces from it.

**Input:** One line string s.

**Output:** String without spaces.

**Sample Test Cases:**

Sample 1
```text
Input:
I love Python

Output:
IlovePython
```

Sample 2
```text
Input:
a b c

Output:
abc
```

**Python Solution:**
```python
s = input()
print(s.replace(" ", ""))
```

## 80. First Non-Repeating Character
- [ ] Done
**Problem Statement:** Given a string, print the first character that appears exactly once. If none, print None.

**Input:** One line string s.

**Output:** First non-repeating character or None.

**Sample Test Cases:**

Sample 1
```text
Input:
swiss

Output:
w
```

Sample 2
```text
Input:
aabb

Output:
None
```

**Python Solution:**
```python
s = input()
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

ans = "None"
for ch in s:
    if freq[ch] == 1:
        ans = ch
        break
print(ans)
```

## 81. Anagram Check
- [ ] Done
**Problem Statement:** Given two strings, check whether they are anagrams. Ignore spaces and case.

**Input:** Two lines, strings a and b.

**Output:** Yes or No.

**Sample Test Cases:**

Sample 1
```text
Input:
Listen
Silent

Output:
Yes
```

Sample 2
```text
Input:
apple
pale

Output:
No
```

**Python Solution:**
```python
a = input().replace(" ", "").lower()
b = input().replace(" ", "").lower()
print("Yes" if sorted(a) == sorted(b) else "No")
```

## 82. Digit Count in String
- [ ] Done
**Problem Statement:** Given a string, count how many characters are digits.

**Input:** One line string s.

**Output:** Number of digit characters.

**Sample Test Cases:**

Sample 1
```text
Input:
abc123

Output:
3
```

Sample 2
```text
Input:
hello

Output:
0
```

**Python Solution:**
```python
s = input()
print(sum(1 for ch in s if ch.isdigit()))
```

## 83. Alphabet Count
- [ ] Done
**Problem Statement:** Given a string, count how many characters are English letters.

**Input:** One line string s.

**Output:** Number of alphabetic characters.

**Sample Test Cases:**

Sample 1
```text
Input:
abc123XYZ

Output:
6
```

Sample 2
```text
Input:
12@#

Output:
0
```

**Python Solution:**
```python
s = input()
print(sum(1 for ch in s if ch.isalpha()))
```

## 84. Capitalize Words
- [ ] Done
**Problem Statement:** Given a sentence, capitalize the first letter of every word.

**Input:** One line sentence.

**Output:** Capitalized sentence.

**Sample Test Cases:**

Sample 1
```text
Input:
hello world

Output:
Hello World
```

Sample 2
```text
Input:
python is fun

Output:
Python Is Fun
```

**Python Solution:**
```python
s = input()
print(s.title())
```

## 85. Replace Character
- [ ] Done
**Problem Statement:** Given a string, a character old, and a character new, replace all old with new.

**Input:** First line string s. Second line old new.

**Output:** Modified string.

**Sample Test Cases:**

Sample 1
```text
Input:
banana
a o

Output:
bonono
```

Sample 2
```text
Input:
hello
l x

Output:
hexxo
```

**Python Solution:**
```python
s = input()
old, new = input().split()
print(s.replace(old, new))
```

## 86. Longest Word
- [ ] Done
**Problem Statement:** Given a sentence, print the longest word. If multiple, print the first one.

**Input:** One line sentence.

**Output:** Longest word.

**Sample Test Cases:**

Sample 1
```text
Input:
I love programming

Output:
programming
```

Sample 2
```text
Input:
one two six

Output:
one
```

**Python Solution:**
```python
words = input().split()
longest = words[0]
for word in words:
    if len(word) > len(longest):
        longest = word
print(longest)
```

## 87. String Starts With
- [ ] Done
**Problem Statement:** Given two strings s and prefix, check whether s starts with prefix.

**Input:** First line s. Second line prefix.

**Output:** Yes or No.

**Sample Test Cases:**

Sample 1
```text
Input:
programming
pro

Output:
Yes
```

Sample 2
```text
Input:
python
java

Output:
No
```

**Python Solution:**
```python
s = input()
prefix = input()
print("Yes" if s.startswith(prefix) else "No")
```

## 88. String Ends With
- [ ] Done
**Problem Statement:** Given two strings s and suffix, check whether s ends with suffix.

**Input:** First line s. Second line suffix.

**Output:** Yes or No.

**Sample Test Cases:**

Sample 1
```text
Input:
filename.py
.py

Output:
Yes
```

Sample 2
```text
Input:
hello
he

Output:
No
```

**Python Solution:**
```python
s = input()
suffix = input()
print("Yes" if s.endswith(suffix) else "No")
```

## 89. Remove Duplicate Characters
- [ ] Done
**Problem Statement:** Given a string, remove duplicate characters while keeping first occurrence order.

**Input:** One line string s.

**Output:** String after removing duplicate characters.

**Sample Test Cases:**

Sample 1
```text
Input:
banana

Output:
ban
```

Sample 2
```text
Input:
programming

Output:
progamin
```

**Python Solution:**
```python
s = input()
seen = set()
ans = []
for ch in s:
    if ch not in seen:
        seen.add(ch)
        ans.append(ch)
print("".join(ans))
```

## 90. Toggle Case
- [ ] Done
**Problem Statement:** Given a string, convert lowercase letters to uppercase and uppercase letters to lowercase.

**Input:** One line string s.

**Output:** Toggled string.

**Sample Test Cases:**

Sample 1
```text
Input:
PyThOn

Output:
pYtHoN
```

Sample 2
```text
Input:
Hello 123

Output:
hELLO 123
```

**Python Solution:**
```python
s = input()
print(s.swapcase())
```

## 91. Right Triangle Stars
- [ ] Done
**Problem Statement:** Given n, print a right triangle of stars with n rows.

**Input:** One integer n.

**Output:** Pattern of stars.

**Sample Test Cases:**

Sample 1
```text
Input:
4

Output:
*
**
***
****
```

**Python Solution:**
```python
n = int(input())
for i in range(1, n + 1):
    print("*" * i)
```

## 92. Square Stars
- [ ] Done
**Problem Statement:** Given n, print an n by n square of stars.

**Input:** One integer n.

**Output:** Pattern of stars.

**Sample Test Cases:**

Sample 1
```text
Input:
3

Output:
***
***
***
```

**Python Solution:**
```python
n = int(input())
for _ in range(n):
    print("*" * n)
```

## 93. Number Triangle
- [ ] Done
**Problem Statement:** Given n, print rows where row i contains numbers from 1 to i.

**Input:** One integer n.

**Output:** Number triangle.

**Sample Test Cases:**

Sample 1
```text
Input:
4

Output:
1
1 2
1 2 3
1 2 3 4
```

**Python Solution:**
```python
n = int(input())
for i in range(1, n + 1):
    print(*range(1, i + 1))
```

## 94. Inverted Triangle Stars
- [ ] Done
**Problem Statement:** Given n, print an inverted right triangle of stars.

**Input:** One integer n.

**Output:** Pattern of stars.

**Sample Test Cases:**

Sample 1
```text
Input:
4

Output:
****
***
**
*
```

**Python Solution:**
```python
n = int(input())
for i in range(n, 0, -1):
    print("*" * i)
```

## 95. Dictionary Frequency
- [ ] Done
**Problem Statement:** Given n words, print each distinct word and its frequency in first occurrence order.

**Input:** First line n. Next n lines contain one word.

**Output:** Each line: word frequency.

**Sample Test Cases:**

Sample 1
```text
Input:
5
cat
dog
cat
bird
dog

Output:
cat 2
dog 2
bird 1
```

**Python Solution:**
```python
n = int(input())
freq = {}
order = []
for _ in range(n):
    word = input().strip()
    if word not in freq:
        freq[word] = 0
        order.append(word)
    freq[word] += 1

for word in order:
    print(word, freq[word])
```

## 96. Student Pass Count
- [ ] Done
**Problem Statement:** Given marks of n students, count how many passed. Passing mark is 40.

**Input:** First line n. Second line n marks.

**Output:** Number of students who passed.

**Sample Test Cases:**

Sample 1
```text
Input:
5
50 35 80 20 40

Output:
3
```

Sample 2
```text
Input:
3
10 20 30

Output:
0
```

**Python Solution:**
```python
n = int(input())
marks = list(map(int, input().split()))
print(sum(1 for m in marks if m >= 40))
```

## 97. Simple Login
- [ ] Done
**Problem Statement:** Given username and password, print Login Successful if username is admin and password is 1234, otherwise Login Failed.

**Input:** Two lines: username and password.

**Output:** Login Successful or Login Failed.

**Sample Test Cases:**

Sample 1
```text
Input:
admin
1234

Output:
Login Successful
```

Sample 2
```text
Input:
admin
1111

Output:
Login Failed
```

**Python Solution:**
```python
username = input().strip()
password = input().strip()

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Login Failed")
```

## 98. BMI Category
- [ ] Done
**Problem Statement:** Given weight in kg and height in meters, calculate BMI and print category: Underweight if <18.5, Normal if <25, Overweight if <30, otherwise Obese.

**Input:** Two floats weight and height.

**Output:** BMI category.

**Sample Test Cases:**

Sample 1
```text
Input:
70 1.75

Output:
Normal
```

Sample 2
```text
Input:
95 1.70

Output:
Obese
```

**Python Solution:**
```python
weight, height = map(float, input().split())
bmi = weight / (height * height)

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")
```

## 99. Simple Password Strength
- [ ] Done
**Problem Statement:** Given a password, print Strong if it has at least 8 characters, at least one digit, and at least one uppercase letter. Otherwise print Weak.

**Input:** One line password.

**Output:** Strong or Weak.

**Sample Test Cases:**

Sample 1
```text
Input:
Hello123

Output:
Strong
```

Sample 2
```text
Input:
hello

Output:
Weak
```

**Python Solution:**
```python
password = input()
has_digit = any(ch.isdigit() for ch in password)
has_upper = any(ch.isupper() for ch in password)

if len(password) >= 8 and has_digit and has_upper:
    print("Strong")
else:
    print("Weak")
```

## 100. Matrix Sum
- [ ] Done
**Problem Statement:** Given a matrix with r rows and c columns, print the sum of all elements.

**Input:** First line r c. Next r lines contain c integers.

**Output:** Sum of matrix elements.

**Sample Test Cases:**

Sample 1
```text
Input:
2 3
1 2 3
4 5 6

Output:
21
```

Sample 2
```text
Input:
1 2
10 20

Output:
30
```

**Python Solution:**
```python
r, c = map(int, input().split())
total = 0
for _ in range(r):
    row = list(map(int, input().split()))
    total += sum(row)
print(total)
```
