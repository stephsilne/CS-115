from cs115 import *

def special (x):

    if x == 42:
        return " very boring"
    else:
      return "lol"
    
        
def odd (n):

    return n % 2 == 1

L1 = [1,2,3,4,5,6,7,8,9]


def primeornot(n):
    l = filter(lambda x: n % x == 0, range(2,n))
    return len(l) == 0


assert(primeornot(7) == True)

def sign(n):
    if n < 0:
        return -1
    else:
        return 1


def make(n):
    for i in range(0,n):
        break
