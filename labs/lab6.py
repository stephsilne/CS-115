'''
@author:   Stephaan Silne
Pledge:    "I pledge my honor that I have abided by the Stevens Honor System"

CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    return not n % 2 == 0
    '''returns the opposite of the true statement that n is divisible by 2 without a remainder, thus it is checking if its odd'''

'''base-2 representation of 42 = 101010'''
'''given an odd base-10 number, the rightmost bit is 1'''
'''given an even base-10 number, the rightmost bit is 0'''
'''given an odd base-10 number, deleting the rightmost bit gives (n-1)/2'''
'''given an even base-10 number, deleting the rightmost bit gives n/2'''
'''if N is odd, we can easily find the base-2 rep. of N by adding the 1 to the base-2 of Y'''
'''if N is even, we can easily find the base-2 rep. of N by adding 0 to the base-2 of Y'''

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        '''if the number given is 0'''
        return ''
        '''only an empty string can be returned as its binary representation'''
    elif isOdd(n):
        '''otherwise if the number given is odd'''
        return numToBinary(n//2) + '1'
        '''recursively return the binary representation of n divided by 2(integer) plus 1'''
    else:
        return numToBinary(n//2) + '0'
        '''recursively return the binary representation of n divided by 2(integer) plus 0 if n given is not odd, i.e. is even'''
        

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        '''if the binary string given is blank'''
        return 0
        '''return the value of 0 as it represents a empty string in decimal'''
    elif s[-1] == '1':
        '''if the last element of the binary string is 1, meaning its odd'''
        return 2*binaryToNum(s[:-1]) + int(s[-1])
        '''return 2^0 times the last element 's[-1]' and then recursively multiply the power 2^n to the rest of the binary string'''
    else:
        return 2*binaryToNum(s[:-1])
        '''otherwise, the binary string represents an even number so return 2^0 times 0 plus the recursive function multiplied by the power of 2^n'''


def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    if s == '':
        '''if the binary string is empty, then an empty string must be returned as the next highest value'''
        return ''
        '''returns an empty string which is the next highest value of nothing'''
    elif binaryToNum(s) == 255:
        '''otherwise if the decimal value of the binary is the highest value an 8bit number can be, which is 255'''
        return ('0' * 8)
        '''return a string of 8 zero's'''
    else:
        digits = numToBinary(binaryToNum(s) + 1)
        '''deifnes digit which turns the conversion of binary string s to a number, then adds 1 and then converts that to binary'''
        return ('0' * (8-len(digits))) + digits
        '''returns digit and then adds 0 times the number of the rest remaining places that 0 should fill for it to be an 8 bit binary string'''
        

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    if not n >= 0:
        '''if the precondition is not met, then an empty string should be given'''
        return ' '
        '''returns an empty string as this is how much 'nothing' can be incremented'''
    else:
      print(s)
      '''prints s, as this is the increment if n = 0'''
      count(increment(s),n-1)
      '''recursively 'returns' the count of the rest of the increments n-1 to s using increment function'''
      

'''the tenary rep. of 59 is 2012 because there are 2 ones, 1 three, 0 nines, and 2 twenty-sevens'''
def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n == 0:
        '''if n equals 0, then an empty string should be returned'''
        return ''
        '''returns the corresponding value which is an empty string'''
    else:
        return numToTernary(n//3) + str(n % 3)
        '''otherwise returns the recursive function of n integer divided by 3 plus the value of the remainder converted to a string'''

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        '''if the binary string is empty, then the corresponding value in decimal is 0'''
        return 0
        '''returns 0 as this is the decimal value for an empty string'''
    else:
        return 3*ternaryToNum(s[:-1]) + int(s[-1])
        '''otherwise return 3^0 times the last element of the string, and then add that to 3^n of the rest of the binary string'''
    
