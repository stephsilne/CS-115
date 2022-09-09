from cs115 import *

def LCS (s1, s2):
    if s1 == '' or s2 == '':
        return 0
    elif s1[0] == s2[0]:
        return 1 +LCS(s1[1:], s2[1:])
        '''if the first element of both strings match, see if any other characters in the string match'''
        '''being 'greedy'''
    else:
        use = LCS(s1[1:],s2)
        lose = LCS(s1, s2[1:])
        return max(use, lose)

def testLCS():
    assert LCS("spam","sam!") == 3


def exp(n,k):
    if k == 0:
        return 1
    else:
        return n * exp(n, k-1)
        
def expfast(n,k):
    if k == 0:
        return 1
    elif k % 2 == 0:
        t = expfast(n, k//2)
        return t*t
    else:
        return n * expfast(n,k-1)

def testExp():
    assert exp(3,5) == 3**5

#TAIL RECURSION

def exptail(n,k):
    def ext(accumulator,n,k):
        if k == 0:
            return accumulator
        else:
            return ext(n * accumulator, n, k-1)
    return ext(1,n,k)

