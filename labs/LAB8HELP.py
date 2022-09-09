from cs115 import*

def fib_printer(n):
    for i in range(n):
        print(fib(i))


def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
