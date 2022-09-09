from cs115 import *
import math

'''"I pledge my honor that I have abided by the Stevens Honor System" Stephaan Silne'''
def dot (L,K):
    '''defines the dot function'''
    if L == [] or K == []:
        '''evaluates if L or K are empty lists'''
        return 0.0
        '''returns the value of zero if the case is true'''
    else:
        '''evaluates if the first case is false'''
        result = L[0] * K[0]
        '''multiplies the first indexes of both L and K'''
        return result + (dot(L[1:],K[1:]))
    '''returns the result and adds it to the dot product of index and 1 and onward'''

def length (M):
    if M == []:
        return 0
    else:
        return 1 + length(M[1:])


def explode (S):
    '''defines the explode function'''
    if S == '':
        '''evaluates if S given is an empty string'''
        return []
        '''returns an empty list as a result'''
    else:
        '''evaluates if the 'if' statement is false'''
        return [S[0]] + explode (S[1:])
    '''returns the first index plus the 'exploded' remaining indexes from 1 onward'''
        
def ind (e, L):
    '''defines the 'ind' function'''
    if L == [] or L == '':
        '''evaluates if the 'L' given is empty list or empty string'''
        return 0
        '''returns zero if this is the case'''
    elif L[0] == e:
        '''otherwise if the first index is e'''
        return 0
        '''return the value 0 if 'elif' is true'''
    else:
        '''evaluates if the first cases are false'''
        return 1 + ind (e, L[1:])
    '''returns 1 plus the value of the index for e'''

def removeAll (e,L):
    '''defines removeAll function'''
    if L == []:
        '''evaluates if the list 'L' given is an empty list'''
        return []
        '''returns an empty list back if the case is true'''
    elif L[0] == e:
        '''evaluates if otherwise the first index of the list is e'''
        return removeAll(e, L[1:])
        '''returns the removal of e, and then further evaluates from index 1 and onward'''
    else:
        '''if those statements are not true'''
        return [L[0]] + removeAll(e, L[1:])
        '''returns the first index of the list and the removeAll function to index 1 and onward'''
    

def myFilter (f,L):
    '''defines myFilter'''

    if L == []:
        '''evaluates if L given is an empty list'''
        return []
        '''returns an empty list in result'''
    elif f(L[0]) == True:
        '''evaulates also, if the first index as a function of 'f' yeilds a true statement'''     
        return [L[0]] + myFilter(f, L[1:])
        '''returns the first index along with the recursion of idexes 1 and onward'''
    else:
        '''if the cases are false'''
        return myFilter (f,L[1:])
        '''returns myFilter evaluating the function 'f' over the list from index 1 and onward'''

def deepReverse (L):
    '''defines deepReverse'''
    if L == []:
        '''evaluates if L given is an empty list'''
        return []
        '''returns an empty list in result'''
    elif isinstance (L[0],list):
        '''evaluates otherwise, if there is an instance that the first index is a list within a list'''
        return deepReverse (L[1:]) + [deepReverse(L[0])]
        '''returns deepReverse of index 1 onward plus the deepReverse of the imbedded list'''
    else:
        '''if those cases are not true'''
        return deepReverse (L[1:]) + [L[0]]
        '''returns deepReverse of index 1 and onwards added to the first index'''
     





