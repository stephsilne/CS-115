'''Stephaan Silne'''
'''I pledge my honor that I have abided by the Stevens Honor System'''


from cs115 import *

def pascal_row(n):
    '''defines the function pascal_row which takes in an integer n greater than 0'''
    if n < 0:
        '''if input 'n' is less than 0, an empty list should be given'''
        return []
        '''returns an empty list as pascal's triangles rows cannot be given for n < 0'''
    elif n == 0:
        '''otherwise if the input given is 0, return the 0th row'''
        return [1]
        '''returns the value of the 0th row in a list'''
    else:
        return [1] + pas_cal(pascal_row(n-1)) + [1]
        '''if those initial statments are not met; else return a list composed of the first element as 1, the last element as 1 and the middle being the sum of the previous rows element using the function pas_cal'''
    

def pas_cal(A) :
    '''defines pas_cal which takes in a list as input'''
    if length(A) == 1:
        '''if the length of the input is 1, or if there is only one element in the list'''
        return []
        '''return an empty list given that adjacent sums cant be made from one element'''
    else :
        return [(A[0]+A[1])] + pas_cal(A[1:])
        '''otherwise return the sum of the first two elements of the list and recursively do the same ot th erest of the list given'''

def length(M):
    '''defines the length function that takes a list as input and reutrns its length'''
    if M == []:
        '''if an empty list is given'''
        return 0
        '''return the value of 0, as a list without any elements has no length'''
    else:
        return 1 + length(M[1:])
        '''else add 1 (representing the length of the first element and recursively compute the length of the rest of the list'''
        

def pascal_triangle(m):
    '''deines pascal_triangle with takes in an integer m, and returns rows of pascal leading to that number'''
    if m < 0:
        '''if the integer given is less than 0, no rows can be given'''
        return []
        '''return an empty list given that 0th rows and on can only be evaluated'''
    if m == 0:
        '''if the input given is 0'''
        return [[1]]
        '''return a list containing a sublist which is the value of the 0th row in pascal's triangle'''
    else:
        return pascal_triangle(m-1) + [pascal_row(m)]
        '''otherwise recursively compute pascal's triangle of the m-th row minus 1, plus the pascal_row of the m-th row'''


def test_pascal_row():
    '''tests the pascal_row function under several conditions using several asserts'''
    assert pascal_row(5) == [1,5,10,10,5,1]
    assert pascal_row(1) == [1,1]
    assert pascal_row(3) == [1,3,3,1]
    assert pascal_row(6) == [1,6,15,20,15,6,1]
    


def test_pascal_triangle():
    '''tests the pascal_triangle function under several conditions using several asserts'''
    assert pascal_triangle(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
    assert pascal_triangle(1) == [[1],[1,1]]
    assert pascal_triangle(0) == [[1]]
    assert pascal_triangle(2) == [[1],[1,1],[1,2,1]]
