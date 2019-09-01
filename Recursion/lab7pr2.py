import time

def F(n):
    #base case
    if n <= 1:
        return n
    #recursive case
    else:
        return (F(n-1) + F(n-2))

def f(n):
    n1 = 0
    n2 = 1
    #case 1
    if n < 0:
        return 'Incorrect input'
    #case 2
    elif n == 0:
        return n1
    #case 3
    elif n == 1:
        return n2
    #implementation of sequence
    else:
        for i in range(1, n):
            nth = n1 + n2
            n1 = n2
            n2 = nth
        return n2
    

start = time.time()
f(40)
end = time.time()
print(end - start)
