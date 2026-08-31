# make a recursive funciton so that i prints fibonacci number till n

def fibo_recursive(left, right):
    global count # global counter as we already have 0 1 starting form 2
    global n # the last one
    if count <= n: # as long as its not the last number input by user
        print(left, end=", ") # print the values till the n
        left, right = right, left + right # do the addition of lef and right number and move forward by swapping the new fibo value to right and current right to left, thus its moves forward
        count += 1 # increase counter one step ahead each time until the counter passes the n
        fibo_recursive(left, right) # call the fibo funciton with the updated lef t and right value do the same thing.
    else:
        return # when done doing till n 


if __name__=="__main__":
    left = 0
    right = 1
    count = 2
    n = int(input())
    fibo_recursive(left, right)