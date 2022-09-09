from cs115 import*

def stutter (L):
    if L == []:
        return []
    else:
        return  [L[0],L[0]]+ stutter(L[1:])
    

def prime (n):
    '''whether or not n is prime, assuming n is a non-negative integer'''
    possDivs = range (1,n)
    divs = filter (divides(n), possDivs)
    return sum(divs) == 1


def divides (n):
    '''returns a function that tests whether a number is divisible by n'''
    def div (k):
        '''whether k is divisible by n'''

        return n % k == 0

    return div
