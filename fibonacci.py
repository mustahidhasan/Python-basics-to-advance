# find the fibonacci serise till the number n, 0, 1, 1, 2, 3, 5, 8, 13, 21, ....... 
# steps to resolve it; 
# 1. Fibonacci serise starts from 0 , 1 
# 2. add two number and create a new fibonacci value
# 3. update the left and right flag with new fibonacci value and previous number do it till n

# basic solution
def basic_fibonacci(n):
    left = 0
    right = 1
    for _ in range(n):
        print(left, end=", ")
        fibonacci = left + right
        left = right
        right = fibonacci

def pro_fibonacci(n):
    left, right = 0, 1
    for _ in range(n):
        print(left, end=", ")
        left, right = right, left + right # right becomes left , sum of left right becomes the new right
        

if __name__ == "__main__":
    n = int(input())
    print("BASIC FIBONACCI")
    basic_fibonacci(n)
    print()
    print("PRO FIBONACCI")
    pro_fibonacci(n)
    print()

