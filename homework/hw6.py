'''
@author:   Stephaan Silne
Pledge: "I pledge my honor that I have abided by the Stevens Honor System"
CS115 - Hw 6
'''

# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

from cs115 import *

'''Tests'''
Penguin: "00011000"+"00111100"*3 + "01111110"+"11111111"+"00111100"+"00100100"
Smile: "0"*8 + "01100110"*2 + "0"*8 + "00001000" + "01000010" + "01111110" + "0"*8
Five: "1"*9 + "0"*7 + "10000000"*2 + "1"*7 + "0" + "00000001"*2 + "1"*7 + "0"
Pizza: "0001"*16 + "1000"*16 + "0010" *16 + "1001"*16

def compress(s):
    '''defines compress which takes as input a 64 bit binary string and outputs the compression of the image'''
    list_s = list_change(com_press(s))
    '''returns a new list, containing the amount of character and character plus [0,0] if the list begins with a 1'''
    if len(map(compressor,list_s)) > 1:
        '''if the length of the list is greater than one, meaning theres multiple 0's or multiple 1's in the list'''
        return reduce(lambda x,y: x+y, (map(compressor,list_s)))
        '''return a string containing all of these binary values that describe how many consecutive 1's and 0's there are'''
    else:
        bins = map(compressor,list_s)
        '''defines bins which just maps compressor(helper function') to our new list'''
        return bins[0]
        '''returns the first element of bins which is essentially bins but without the bracket to indicate its a list'''

def compressor(M):
    '''defines compressor which takes [how many of,0 or 1] and returns 'how many of' in a binary string'''
    if M == []:
        '''if the element is empty, then this helper function cant work, therefore dont return anything'''
        return []
        '''returns an empty list'''
    if len(numToBinary(M[0])) < 5:
        '''if the length of the binary repres. of the amount is less than five'''
        digits = numToBinary(M[0])
        '''establishes digits which is the binary repres. of the amount of 0's or 1's'''
        return ('0' * (5 - len(digits))) + digits
        '''return this less than 5 binary string and fill in the rest of the characters with zero's'''
    if len(numToBinary(M[0])) == 5:
        '''if the length of the binary repres. is equal to 5, do nothing'''
        return numToBinary(M[0])
        '''returns just the binary repres. of how many 0's or 1's'''
    if len(numToBinary(M[0])) > 5:
        '''if the length is greater than 5, meaning there are only 0's or only 1's in the original string'''
        num = (M[0])//31
        '''establishes num which finds out how many 31's (largest value given by a 5 bit string) there are in this decimal repres. of how many'''
        rem = (M[0])% 31
        '''establishes rem which gives the remainder of the previous calculation'''
        val = num * [31] + [rem]
        '''establishes val which gives 'how many' in a broken down list, containing however many 31's and the rest'''
        chng_val = addzeros(val)
        '''defines chng_val which adds zeros in between given that there could be 31 zeros and then 0 ones and then 31 more zeros....'''
        new_elem = map (mustFive, chng_val)
        '''established new_elem, which takes sure than each of these broken down numbers are given in 5 bit strings'''
        return reduce(lambda x,y: x + y, new_elem)
        '''reduces this list into a single string that represents how many 0's or 1's there are for the compressed image'''
    
def addzeros(L):
    '''defines addzeros which adds zeros between elements in a list recursively'''
    if len(L) == 1:
        '''if the length of the list is one, nothing can be added between one and itself'''
        return L
        '''therefore,just return the list of one element given'''
    else:
        return [L[0]] + [0] + addzeros(L[1:])
        '''otherwise add the first element of the list, a list containing the element '0' and then compute this recursively to the rest of the list'''
def mustFive(v):
    '''defines mustFive which makes sure that the binary string given is 5 bit'''
    if len (numToBinary(v)) < 5:
        '''if the length of v is less than 5'''
        return ('0' * (5-len(numToBinary(v)))) + numToBinary(v)
        '''return this less than 5 binary string and fill in the rest of the characters with zero's'''
    else:
        return numToBinary(v)
        '''otherwise just return the binary string as it already fits the condition'''

def list_change(L):
    '''defines list_change which takes as input a list and if the first element is a 1, returns [0,0] plus that list'''
    if L[0][1] == '1':
        '''if the first element of the string given is a 1'''
        return [[0,'0']] + L
        '''return [0,'0'] plus that list to show that there are zero 0's and however many 1's in the list given'''
    else:
        return L
        '''if these cases are not met, just return the list'''
    
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


def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    return not n % 2 == 0
    '''returns the opposite of the true statement that n is divisible by 2 without a remainder, thus it is checking if its odd'''

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

def com_press(s):
    '''defines com_press which takes in a non-empty 64bit string consisting of 1's and 0's and returns [how many,char]''' 
    if s == '':
        '''if the string given is empty, nothing can be computed'''
        return
        '''returns nothing, continues with other cases'''
    if len(s) == 1:
        '''if the length of the string is 1, then it should return a list consisting of the number of times the element occurs in thr string (once) and the element itself'''
        return [[1,s[0]]]
        '''returns list of '1' as in how many and the element itself'''
    c = com_press(s[:-1])
    '''establishes c as the recursive function call to com_press to compute upon every element of the string except the last'''
    if c[-1][1] != s[-1]:
        '''if the last element of the list given by com_press,index at 1, does not equal the last element of the string'''
        return c + [[1,s[-1]]]
        '''the function should continue recursively and note that there is only one occurrence of that last element, adding them together'''
    else:
        c[-1][0] = c[-1][0] + 1
        '''increments the last element of com_press,indexed at 0, if the both elements were indeed equal, meaning the element occurred more than once''' 
        return c
        '''recursively calls c to com_press the rest of the list, except the last element'''

def uncompress(C):
    '''defines uncompress which decompress a string to its original format'''
    if len(C) == 0:
        '''if the length of the compressed string is 0, then nothing can be uncompressed'''
        return ''
        '''returns an empty string to signify'''
    else:
        return ('0' * binaryToNum(C[0:5])) + ('1' * binaryToNum(C[5:10])) + uncompress(C[10:])
        '''otherwise multiply '0' by the decimal version of the first 5 elements and then multiply '1' by the decimal version of the next 5, and then recursively do this to the rest of the list to completly uncompress'''
def compression(s):
    '''defines compression which returns the ratio of sizes(lengths) of the compressed string and its original format'''
    return (len(compress(s)))/(len(s))
    '''returns the division of the length of compressed string and the length of the original string'''


'''Professor Lai is lying about being able to create a compression algorithm that takes in 64bits and returns a shorter one, because compressing an image even further wouldnt be able to create the original image if it was uncompressed.''' 

