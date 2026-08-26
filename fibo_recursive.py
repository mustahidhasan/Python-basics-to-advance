# make a recursive funciton so that i prints fibonacci number till n

def fibo_recursive(left, right):
    global count
    global n
    if count <= n:
        print(left, end=", ")
        left, right = right, left + right
        count += 1
        fibo_recursive(left, right)
    else:
        return


if __name__=="__main__":
    left = 0
    right = 1
    count = 2
    n = int(input())
    fibo_recursive(left, right)