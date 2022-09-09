from cs115 import*


def primeornot(n):
    divisors = filter(lambda x: n % x == 0, range(2,n))
    return len(divisors) == 0

