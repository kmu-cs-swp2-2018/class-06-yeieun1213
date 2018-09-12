import time
import random

def fibo(n):
    if n<= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

def iterfibo(n):
    y = 0
    z = 1
    num = 0

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(n - 1):
            num = y + z
            y = z
            z = num
        return num

while True:
    nbr = int(input("Enter a number:"))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = iterfibo(nbr)
    ts = time.time() - ts
    print("IterFibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))