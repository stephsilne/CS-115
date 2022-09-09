'''Stephaan Silne'''
'''I pledge my honor that I have abided by the Stevens Honor System'''

from cs115 import*


#EXERCISE 1
def numToBaseB(N,B):
    '''defines numToBaseB which takes as input a number N in decimal representation and a base B, to which it converts'''
    if N == 0:
        '''if N equals 0, then the binary value of 0 should be given for all bases'''
        return 0
        '''returns 0 given that the decimal number given is 0'''
    if B == 2:
        '''if the base given is 2'''
        return numToBase2(N)
        '''apply the function numToBase2 to the number given as input'''
    if B == 3:
        '''if the base given is 3'''
        return numToBase3(N)
        '''apply the function numToBase3 to the number N given as input'''
    if B == 4:
        '''if the base given is 4'''
        return numToBase4(N)
        '''apply the function numToBase4 to the number N given as input'''
    if B == 5:
        '''if the base given is 5'''
        return numToBase5(N)
        '''apply the function numToBase5 to the number N given as input'''
    if B == 6:
        '''if the base given is 6'''
        return numToBase6(N)
        '''apply the function numToBase6 to the number N given as input'''
    if B == 7:
        '''if the base given is 7'''
        return numToBase7(N)
        '''apply the function numToBase7 to the number N given as input'''
    if B == 8:
        '''if the base given is 8'''
        return numToBase8(N)
        '''apply the function numToBase8 to the number N given as input'''
    if B == 9:
        '''if the base given is 9'''
        return numToBase9(N)
        '''apply the function numToBase9 to the number N given as input'''
    if B == 10:
        '''if the base given is 10'''
        return numToBase10(N)
        '''apply the function numToBase10 to the number N given as input'''

def isOdd(n):
    '''defines the function 'isOdd' which takes as input n and relays if a number is odd if the boolean statement is not met'''
    return not n % 2 == 0
    '''returns true if the remainder of n divided by 2 does not equal 0, meaning it is odd'''

def numToBase2(n):
    '''defines numToBase2 which takes a number n is decimal representation and returns its binary representation in base 2'''
    if n == 0:
        '''if n equals 0, then an empty string should be returned'''
        return ''
        '''returns an empty string for the base case'''
    elif isOdd(n):
        '''if application of 'isOdd' over the number n results in a true statement'''
        return numToBase2(n//2) + '1'
        '''return '1' as the rightmost binary character plus the recursive call of numToBase2 to the integer division of n by the base value'''
    else:
        return numToBase2(n//2) + '0'
        '''if the number given is not odd, then return 0 as its rightmost binary character plus the recursive call of numToBase2 to the integer division of n by the base value'''
    
def numToBase3(n):
    '''defines numToBase3 which takes a number n is decimal representation and returns its binary representation in base 3'''
    if n == 0:
        '''if n equals 0, then an empty string should be returned'''
        return ''
        '''returns an empty string for the base case'''
    else:
        return numToBase3(n//3) + str(n%3)
        '''returns the string of the remainder of n divided by 3 for the rightmost character plus the recursive call of numToBase3 to the integer division of n by the base value'''
        
def numToBase4(n):
    '''defines numToBase4 which takes a number n is decimal representation and returns its binary representation in base 4'''
    if n == 0:
        '''if n equals 0, then an empty string should be returned'''
        return ''
        '''returns an empty string for the base case'''
    else:
        return numToBase4(n//4) + str(n%4)
        '''returns the string of the remainder of n divided by 4 for the rightmost character plus the recursive call of numToBase4 to the integer division of n by the base value'''
        
    
def numToBase5(n):
    '''defines numToBase5 which takes a number n is decimal representation and returns its binary representation in base 5'''
    if n == 0:
        '''if n equals 0, then an empty string should be returned'''
        return ''
        '''returns an empty string for the base case'''
    else:
        return numToBase5(n//5) + str(n%5)
        '''returns the string of the remainder of n divided by 5 for the rightmost character plus the recursive call of numToBase5 to the integer division of n by the base value'''
    
def numToBase6(n):
    '''defines numToBase6 which takes a number n is decimal representation and returns its binary representation in base 6'''
    if n == 0:
        '''if n equals 0, then an empty string should be returned'''
        return ''
        '''returns an empty string for the base case'''
    else:
        return numToBase6(n//6) + str(n%6)
        '''returns the string of the remainder of n divided by 6 for the rightmost character plus the recursive call of numToBase6 to the integer division of n by the base value'''
    
def numToBase7(n):
    '''defines numToBase7 which takes a number n is decimal representation and returns its binary representation in base 7'''
    if n == 0:
        '''if n equals 0, then an empty string should be returned'''
        return ''
        '''returns an empty string for the base case'''
    else:
        return numToBase7(n//7) + str(n%7)
        '''returns the string of the remainder of n divided by 7 for the rightmost character plus the recursive call of numToBase7 to the integer division of n by the base value'''
        
        
def numToBase8(n):
    '''defines numToBase8 which takes a number n is decimal representation and returns its binary representation in base 8'''
    if n == 0:
        '''if n equals 0, then an empty string should be returned'''
        return ''
        '''returns an empty string for the base case'''
    else:
        return numToBase8(n//8) + str(n%8)
        '''returns the string of the remainder of n divided by 8 for the rightmost character plus the recursive call of numToBase8 to the integer division of n by the base value'''
        
    
def numToBase9(n):
    '''defines numToBase9 which takes a number n is decimal representation and returns its binary representation in base 9'''
    if n == 0:
        '''if n equals 0, then an empty string should be returned'''
        return ''
        '''returns an empty string for the base case'''
    else:
        return numToBase9(n//9) + str(n%9)
        '''returns the string of the remainder of n divided by 9 for the rightmost character plus the recursive call of numToBase9 to the integer division of n by the base value'''

def numToBase10(n):
    '''defines numToBase10 which takes a number n is decimal representation and returns its binary representation in base 10'''
    if n == 0:
        '''if n equals 0, then an empty string should be returned'''
        return ''
        '''returns an empty string for the base case'''
    else:
        return str(n)
        '''returns the string of the number given, as the conversion of a number in decimal to base 10 is just the number'''

#EXERCISE 2
def baseBtoNum(S,B):
    if S == '':
        '''if the binary string given is blank, no matter the base'''
        return 0
        '''return 0, as this is the decimal value needed for the base case'''
    if B == 2:
        '''if the base given is 2'''
        return base2toNum(S)
        '''apply the function 'base2toNum' onto the string S'''
    if B == 3:
        '''if the base given is 3'''
        return base3toNum(S)
        '''return the application of the function 'base3toNum' onto the string '''
    if B == 4:
        '''if the base given is 4'''
        return base4toNum(S)
        '''apply the function 'base4toNum' to the binary string'''
    if B == 5:
        '''if the base given is 5'''
        return base5toNum(S)
        '''apply the function base5toNum to the binary string S'''
    if B == 6:
        '''if the base 6 is given as input'''
        return base6toNum(S)
        '''return base6toNum of the string S for thr decimal conversion'''
    if B == 7:
        '''if B given is 7 as input'''
        return base7toNum(S)
        '''apply the function base7toNum onto the binary string S'''
    if B == 8:
        '''if B given as input is 8'''
        return base8toNum(S)
        '''apply base8toNum to the binary string for the decimal conversion'''
    if B == 9:
        '''if B given is 9'''
        return base9toNum(S)
        '''apply base9toNum to the binary string'''
    if B == 10:
        '''if the base given is 10'''
        return base10toNum(S)
        '''apply base10toNum to the binary string S given as input'''

def base2toNum(s):
    '''defines the function 'base2toNum' that takes a binary string s and converts the string in base 2 to decimal representation'''
    if s == '':
        '''if the binary string given is blank'''
        return 0
        '''return the value of 0 as it represents a empty string in decimal'''
    elif s[-1] == '1':
        '''if the last element of the binary string is 1, meaning its odd'''
        return 2*base2toNum(s[:-1]) + int(s[-1])
        '''return 2^0 times the last element 's[-1]' and then recursively multiply the power 2^n to the rest of the binary string'''
    else:
        return 2*base2toNum(s[:-1])
        '''otherwise, the binary string represents an even number so return 2^0 times 0 plus the recursive function multiplied by the power of 2^n'''
    
def base3toNum(s):
    '''defines the function 'base3toNum' that takes a binary string s and converts the string in base 3 to decimal representation'''
    if s == '':
        '''if the binary string given is blank'''
        return 0
        '''return the value of 0 as it represents a empty string in decimal'''
    else:
        return 3*base3toNum(s[:-1]) + int(s[-1])
        '''otherwise return 3^0 times the last element of the string, and then add that to 3^n of the rest of the binary string'''
    
def base4toNum(s):
    '''defines the function 'base4toNum' that takes a binary string s and converts the string in base 4 to decimal representation'''
    if s == '':
        '''if the binary string given is blank'''
        return 0
        '''return the value of 0 as it represents a empty string in decimal'''
    else:
        return 4*base4toNum(s[:-1]) + int(s[-1])
        '''otherwise return 4^0 times the last element of the string, and then add that to 4^n of the rest of the binary string'''
    
def base5toNum(s):
    '''defines the function 'base5toNum' that takes a binary string s and converts the string in base 5 to decimal representation'''
    if s == '':
        '''if the binary string given is blank'''
        return 0
        '''return the value of 0 as it represents a empty string in decimal'''
    else:
        return 5*base5toNum(s[:-1]) + int(s[-1])
        '''otherwise return 5^0 times the last element of the string, and then add that to 5^n of the rest of the binary string'''

def base6toNum(s):
    '''defines the function 'base6toNum' that takes a binary string s and converts the string in base 6 to decimal representation'''
    if s == '':
        '''if the binary string given is blank'''
        return 0
        '''return the value of 0 as it represents a empty string in decimal'''
    else:
        return 6*base6toNum(s[:-1]) + int(s[-1])
        '''otherwise return 6^0 times the last element of the string, and then add that to 6^n of the rest of the binary string'''
        
    
def base7toNum(s):
    '''defines the function 'base7toNum' that takes a binary string s and converts the string in base 7 to decimal representation'''
    if s == '':
        '''if the binary string given is blank'''
        return 0
        '''return the value of 0 as it represents a empty string in decimal'''
    else:
        return 7*base7toNum(s[:-1]) + int(s[-1])
        '''otherwise return 7^0 times the last element of the string, and then add that to 7^n of the rest of the binary string'''
    
def base8toNum(s):
    '''defines the function 'base8toNum' that takes a binary string s and converts the string in base 8 to decimal representation'''
    if s == '':
        '''if the binary string given is blank'''
        return 0
        '''return the value of 0 as it represents a empty string in decimal'''
    else:
        return 8*base8toNum(s[:-1]) + int(s[-1])
        '''otherwise return 8^0 times the last element of the string, and then add that to 8^n of the rest of the binary string'''

def base9toNum(s):
    '''defines the function 'base9toNum' that takes a binary string s and converts the string in base 9 to decimal representation'''
    if s == '':
        '''if the binary string given is blank'''
        return 0
        '''return the value of 0 as it represents a empty string in decimal'''
    else:
        return 9*base9toNum(s[:-1]) + int(s[-1])
        '''otherwise return 9^0 times the last element of the string, and then add that to 9^n of the rest of the binary string'''
def base10toNum(s):
    '''defines the function 'base10toNum' that takes a binary string s and converts the string in base 10 to decimal representation'''
    if s == '':
        '''if the binary string given is blank'''
        return 0
        '''return the value of 0 as it represents a empty string in decimal'''
    else:
        return int(s)
        '''returns just the integer of the string given, as converting a base 10 number to decimal is just the number'''
    

#EXERCISE 3
def baseToBase(B1,B2,SinB1):
    '''defines the function baseToBase which takes as input two bases and a string in the first base so that it can be converted to the second base'''
    B1todec = baseBtoNum(SinB1,B1)
    '''defines B1todec which applies baseBtoNum to the string SinB1 so that the binary string can be converted to decimal representation'''
    dec_toB2 = numToBaseB(B1todec,B2)
    '''defines dec_toB2 which applies numToBaseB to the string B1todec so that the number in base 10 can be converted to the second base B2 given as input'''
    return dec_toB2
    '''returns this final conversion'''
                       
#EXERCISE 4
def add(S,T):
    '''defines add which adds two binary strings in base 2 thorugh several conversions and returns the base2 sum'''
    if S and T == '':
        '''if both strings given are empty, then the sum cannot be given'''
        return ''
        '''returns an empty string as result'''
    else:
        S_dec = baseBtoNum(S,2)
        '''defines S_dec which is the base to dec. conversion of the string S using the function baseBtoNum'''
        T_dec = baseBtoNum(T,2)
        '''defines T_dec which is the base to dec. conversion of the string T using the function baseBtoNum'''
        s_um = S_dec + T_dec
        '''defines the variable s_um which is the sum of these two decimal values in base 10'''
        result = numToBaseB(s_um,2)
        '''defines result which is the dec. to base conversion of the s_um using numToBaseB'''
        return result
        '''returns the result if the base case is not met'''

#EXERCISE 5
# Each row has (x,y,carry-in) : (sum,carry-out)
FullAdder = { ('0','0','0') : ('0','0'),
('0','0','1') : ('1','0'),
('0','1','0') : ('1','0'),
('0','1','1') : ('0','1'),
('1','0','0') : ('1','0'),
('1','0','1') : ('0','1'),
('1','1','0') : ('0','1'),
('1','1','1') : ('1','1') }


def addB(s1,s2):
    '''defines the function addB so that it can add two strings S1 and S2 and return its resulting binary addition'''
    if not (s1 and s2):
        '''if either of the two strings given are empty, return the sum of those strings (in the case that the two strings given are not of equal length'''
        return s1 + s2
        '''returns the sum of the two strings if the case happens to be true'''
    sumBit,carryBit = FullAdder[(s1[-1],s2[-1],'0')]
    '''defines the variables sumBit and carryBit which obtain values from the tuples given by the recursive call to FullAdder of the rightmost characters of both strings with a carry in of 0'''
    nextadd = addB(s1[:-1],s2[:-1])
    '''defines variable 'nextadd' which computes the recursive call of addB to the rest of the two strings starting from the right'''
    if carryBit == '1':
        '''if the carryBit resulting from the rightmost addition is 1, (if it was 1 + 1)'''
        lastSumBit = '0'
        '''defines the variable lastSumBit which equals the sum of 1 + 1'''
        return addB(nextadd,'1') + lastSumBit
        '''if the case is true, recursively call addB to sum nextadd and the carryBit plus the string of the lastSumBit which was 0, with this only applying is the rightmost addition was 1 + 1'''
    else:
        return nextadd + sumBit
        '''otherwise compute the recursive call to addB for the rest of the original strings plus the sumBit given by the tuple in FullAdder, (if the rightmost sum is 0+1 or 0+0 or 1+0)'''



        
            
    
        
        
        



