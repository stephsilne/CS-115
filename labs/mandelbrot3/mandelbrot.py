# mandelbrot.py
# Lab 9
#
# Name: Stephaan Silne
'''I pledge my honor that I have abided by the Stevens Honor System'''

# keep this import line...
from cs5png import PNGImage

# start your Lab 9 functions here:

def mult (c,n):
    '''mult uses only a loop and addition to multiply c by the integer n'''
    result = 0
    '''initializes result to 0'''
    for x in range(n):
        '''iterate x from range 0 to n'''
        result = result + c
        '''updates the value of result for each x'''
    return result
    '''returns the final result(multiplication) upon all iterations'''


def update(c,n):
    '''update starts with z = 0 and runs z = z**2 + c for a total of n times. It returns the final z.'''
    z = 0
    '''initializes z to 0'''
    for x in range(n):
        '''iterates x from range 0 to n-1'''
        z = z**2 + c
        '''updates the z variable for however many iterations'''
    return z
    '''returns z upon the finishing of the for loop'''

def inMSet(c,n):
    '''takes as input a complex number 'c' for the update step z = z**2 + c and
    integer n, the maximum number of times to run that step. Then is should return False
    as soon as abs(z) > 2, True if abs(z) < 2 (for n iterations)'''
    z = 0
    for x in range(n):
        '''iterates x from range 0 to n-1'''
        z = z**2 + c
        '''updates the z value by z**2 + c for each iteration'''
        if abs(z) > 2:
            '''if abs(z) > 2, the for loop should stop and return False'''
            return False
            '''returns False'''
    else:
        return True
        '''otherwise returns True upon the final iteration'''
    
    
        
