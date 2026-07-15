# **Problem Statement:** Given n, determine whether it is prime.
n = int(input())

if n < 2:
    print("Not Prime") # if the number is less than 2 its not prime , prime starts from 2
else:
    prime = True
    i = 2
    # assume n = 3:
    #     2 * 2 <= 3 : no, so 3 is prime
    # assume n = 4:
    #     2 * 2 <= 4 yes : enters loop, 4 % 2 == 0 yes, prime false breaks
    # assume n = 5:
    #     2 * 2 <= 5: yes , enters loop  5 % 2 == 0 no, hence no prime false no break, i ++
    #     3 * 3 <= 5: no , so 5 is prime true stays                
    while i * i <= n: 
        if n % i == 0:
            prime = False
            break
        i += 1
    print("Prime" if prime else "Not Prime")