from cs115 import *

def mul(x,y):

    return x * y


def f(n):

    return f(n)

def factorial (n):
    if n == 0:
        return 1
    else:
        return n * factorial (n-1)

"function call mechanism"

def tower (n):
    if n == 0:
        return 1
    else:
        return 2 ** tower(n-1)

def testTower ():
    print (tower(3) == 16)


def reverse (L):

    if L == []:
        return 0

    else:
        return reverse (L[1:]) + [L[0]]

    "PUTTING  a braket of L[0] makes the value a list, allow catenation"



def sumlen(M):

    if M == 0:
        return 0
    else:
        
        return len (M)
    

