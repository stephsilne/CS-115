from cs115 import*

def spam():
    for i in range(0,100):
        print (i)

def spam2():
    summ = 0
    for i in range(0,10):
        summ = summ + i
        print (summ)

def mapSqr(L):
    '''assume L is a list of numbers. Return map(sqr,L)'''
    M = []
    for n in L:
        M = M + [n**2]
    return M
        




assert mapSqr([1,2,3,42]) == [1,4,9,42*42]

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def fibo(n):
    num = 0
    while n > 0:
        if n == 1:
            num += 1
        else:
            num += fibo(n-1) + fibo(n-2)
    return num

# a loop invariant is a condition that is supposed to be true
#each time control is at the 'top of the loop', the code uses assertions
#to express and check invariants.

def iFib(n):
    '''returns fib(n) but imperatively implemented'''
    if n == 0 or n == 1:
        return n
    else:
        prev = 0
        cur = 1
        i = 1
        assert cur == fib(i)and prev == fib(i-1) #loop invariant
        assert 1 <= i <= n
        while i != n:
            cur = cur + prev
            prev = cur - prev
            i += 1
            assert cur == fib(i) and prev== fib(i-1)
            assert 1 <= i <= n
    return cur

#there are two asserts because when the while body is iterated, it wont make sure those asserts are true a second time

password = ''
while password != 'password':
    print('What is the password?')
    password = input()

print('Yes, the password is ' + password + '. You may enter.')



''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def mapSqr(L):
    '''assume L is a list of numbers. Return map(sqr,L)'''
    M = []
    for n in L:
        M = M + [n**2]       #alternate: M.append(n**2)
    assert M == map(lambda n: n**2, L)
    return M
    

def wrongMapSqr(L):
    for i in range(len(L)):
        L[i] = L[i]**2
    return L
def okMapSqr(L):
    M = map(lambda x: x,L) #makes a copy of L
    for i in range(len(L)):
        M[i] = L[i]**2
    return M

yourGrades = [100,100,100]
Y = wrongMapSqr(yourGrades)
print('yourGrades after wrongMapSqr',yourGrades)
'''this prints [10000,10000,10000] because all elements of the original L are
reassigned by wrongMapSqr, it doesnt manipulate a new list, changes the same list given'''


def f():
    L = [1,2,3,4]
    g(L)
    return L

def g(List):
    List[0] = 42

