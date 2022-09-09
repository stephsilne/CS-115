# Exercises using map and reduce - Solutions
from cs115 import *

# Try to implement these functions without using
# recursion.  Just map, reduce, range, lambda,
# and built-in operators like appending strings.

def stutter(strs):
    '''assume strs is a list of strings; 
       return a list of each string appended with itself'''
    if strs == []:
        return []
    else:
        return map (lambda W: 2*W,strs)

def testStutter():
    assert stutter(['penny','nickel','dime']) == \
           ['pennypenny', 'nickelnickel', 'dimedime']

def repeater(L):
    '''assume L is a list of 2-element lists [num,string]
    where num is a positive integer.  
    Return the list of strings, each stuttered that number of times.'''
    if L == []:
        return []
    else:
        result = lambda X: X[0]*X[1]
        return map (result, L)

def testRepeater():
    assert repeater([[1,'a'], [3,'b'], [1,'hi'], [4,'bye']]) == \
           ['a', 'bbb', 'hi', 'byebyebyebye']
    
def pyramid(s,n):
    '''assume s is a string and n is a positive integer.
       Return a list of 1, 2, 3, ... up to n copies of n'''
    if s == '':
        return []
    else:
        return map(lambda val: s * val,range (1,n+1))

def testPyramid():
    assert pyramid('x', 4) == ['x', 'xx', 'xxx', 'xxxx']

def underscore(nstrs):
    '''Given a list of non-empty strings, return a single
    string made by catenating the given strings with an underscore
    between.'''
    if nstrs == []:
        return []
    else:
        return reduce(lambda x,y: x + '_' + y,nstrs)

def testUnderscore():
    assert underscore(['patient', 'focused', 'persistent']) == 'patient_focused_persistent'

def coinNames(coinInfo):
    '''assume coinInfo is a non-empty list of pairs [value,name].
    Return the names, as a single string.'''
    if coinInfo == []:
        return ''
    else:
        return reduce (lambda x,y: x + ' ' + y,map(lambda S: S[1],coinInfo))

def testCoinNames():
    assert coinNames([[1,'penny'],[5,'nickel'],[10,'dime']]) == 'penny nickel dime'

def f1(x):
    if x > 0:
        return True
    else:
        False

def f2(x):
    return x > 0

def sumUp(n):
    if n <= 0:
        return 0
    else:
        return n + sumUp(n-1)

def count(num,List):
    if List == []:
        return 0
    elif List[0] == num:
        return 1 + count(num,List[1:])
    else:
        return count(num,List[1:])

def countSymbol(symbol,string):
    if len(string) == 0:
        return 0
    elif symbol == string[0]:
        return 1 + countSymbol(symbol,string[1:])
    else:
        return countSymbol(symbol,string[1:])

def countPattern(shortString,longString):
    if longString == '':
        return 0
    elif len(longString)< len(shortString):
        return 0
    elif shortString == longString[0:len(shortString)]:
        return 1 + countPattern(shortString,longString[1:])
    else:
        return countPattern(shortString,longString[1:])



def isofNine(p):
    return filter(lambda n: (n-9)%10 == 0, range(1,p+1))
    
def square(x):
    return x**2

def power (k):
    def func(x):
        return x*k
    return func



