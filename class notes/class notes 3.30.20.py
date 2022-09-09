from cs115 import*


def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def printFibs(n):
    '''prints the first n fibonacci numbers, assuming n >= 0'''
    for x in range(n):
        print(fib(x))


def printFibsVsn1(n):
    numPrinted = 0
    while numPrinted != n:
        print (fib(NumPrinted))
        numPrinted += 1


def printFibsVsn3(n):
    numPrinted = 0
    prev,curr = 0,0
    while numPrinted != n:
        print(cur)
        prev,cur = cur, prev + cur
        numPrinted += 1


def printFibsVsn4(n):
    numPrinted = 0
    if n > 0:
        print(0)
        numPrinted += 1
        prev,cur = 0,1
        while numPrinted != n:
            print(cur)
            prev,cur = cur, prev+cur
            numPrinted += 1
        
