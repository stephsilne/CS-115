from cs115 import *

def grass (L):
    if L == []:
        return 0
    else:
        return 1 + grass(L[1:])
    
def repeat (n,x):
    #repeats a list of things into a list a 'n' number of times
    if n % 1 != 0 and n > 0:
        return []
    #returns an empty list given that we want a result to be a list
    else:
        return [x]+ (((n-1) * [x]))
   #argument should ALWAYS get smaller in the else part of the recursion

def test_repeat():

    print (repeat(3,'ha') == 3*['ha'])
    print (repeat(2,42) == 2*[42])

def sum (Lon):

    if Lon == 0:
        return 0
    else:
        L[0] + sum (L[1:])

#map can be used to operate on each individual list in a list of lists
#'isinstance' tells you true or false about an element being a list or int. 




    
