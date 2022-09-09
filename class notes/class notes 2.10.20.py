def divides (m):
    def div(k):
        return m % k == 0
    return div

def primes(n):

    return sieve(range(2,n+1))

def sieve (L):
    if L == []: return []
    else:
        return
    
def why(r):
    if r == 0:
        return True
    else:
        return why (r-1)
    
