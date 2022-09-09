# tail recursion exercise 
from cs115 import *

# Complete the following exercises on paper and pencil.
# Check your work by transferring your solutions to your computer
# Here's an example we already studied.

def exp(n,k):
    '''n**k, assuming k>=0 and n is a number'''
    if k == 0: return 1
    else: return n * exp(n,k-1)

def exptail(n, k):
    '''n**k, implemented using tail recursion.'''
    def ext(accumulator, n, k):
        if k == 0: return accumulator
        else: return ext(n * accumulator, n, k-1)
    return ext(1, n, k)

# Exercise 0: Here's a recursive function.
# Implement the alternate version, using tail recursion.
def sumSq(L):
    '''Assuming L is a list of numbers, return the sum of their squares.'''
    if L==[]: return 0
    else: return L[0]**2 + sumSq(L[1:])
    
def sumSq_alt(L):
    def sumsSq(acc,L):
        if L == []:
            return acc
        else:
            return sumsSq((L[0]**2) +acc,L[1:])
    return sumsSq(0,L)

def test():
    t0 = [2,4]
    t1 = range(5)
    assert sumSq(t0) == sumSq_alt(t0)
    assert sumSq(t1) == sumSq_alt(t1)
    

# Exercise 1: Here's another recursive function.
# Implement the alternate version, using tail recursion.

def copies(n, ls):
    '''assuming ls is a list of letters, of length at least n,
    return a list with n copies of the first, n-1 copies of the
    second, etc.  Don't include zero copies.'''
    if n <= 0: return []
    else: return [(n*ls[0])] + copies(n-1, ls[1:])

def testCopies():
    assert copies(3,['a','b','c','d']) == ['aaa', 'bb', 'c']

def copies_alt(n, ls):
    def cps (acc,n,ls):
        if n <= 0:
            return acc
        else:
            return cps(acc + [n*ls[0]],n-1,ls[1:])
    return cps([],n,ls)

def testCopiesAlt():
    L = ['a','b','c','d']
    assert copies_alt(3,L) == copies(3,L)
    assert copies_alt(2,L) == copies(2,L)
