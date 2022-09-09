'''
In-class quiz, March 27, 2020

Stephaan Silne
"I pledge my honor that I have abided by the Stevens Honor System"

Second, read through the rest of the file and follow instructions.

When you're done, the file should load without error in IDLE, even if you weren't able
to solve all the problems.  Upload your file in Canvas.

QUESTION 1: Using four bits, what is the two's complement representation of the number seven?
    A: 0111
    B: 1000
    C: 1111
    D: 0101
    Indicate your answer by putting the right letter in place of x below.
'''

Q1 = 'A'

'''
QUESTION 2: Using four bits, what is the two's complemenet representation of negative three?
    A: 0011
    B: 1100
    C: 1101
    D: 0111
    Indicate your answer by putting the right letter in place of x below.
'''

Q2 = 'C'

'''
QUESTION 3: This is about memoization of a function called LAS which
applies to a string S and a letter ltr.
It returns a longest ascending subsequence of S whose elements are all greater than ltr.
Reminder: characters are compared according to their numerical encoding, which agrees
with alphabetical order in the case of letters. For example, 'a' < 'b' is true
and max('a','b') is 'b'.
Study this test function which shows some correct results from LAS.  The last test
case shows that there can be two maximal ascending subsequences, which is why the
specification says "a longest..." not "the longest...".
'''
def testLAS():
    '''Prints success message or throws exception of failed test.'''
    assert LAS("", 'b') == ""
    assert LAS("bcd", 'd') == ""                # not greater than 'd'
    assert LAS("bcd", 'a') == "bcd"             # ascending and greater than 'a'
    assert LAS("bbccdd", 'a') == "bcd"          # must be strictly ascending
    assert LAS("bdcf", 'a') in [ "bcf", "bdf" ]
      # bcdf has two maximal ascending subsequences
    print("testLAS successful")
'''
Below is a correct implementation of LAS.  Your job is to add code at the ??? places,
so that it uses a dictionary as a memo table.  For keys, your dictionary should
use pairs (S,ltr).  
'''

def LAS(S, ltr):
    '''Assume S is string of letters and ltr is a letter.
       Return a longest subsequence of S that is increasing and 
       whose elements are all greater than ltr.'''
    
    memo = {}

    def helper(S, ltr):

        if (S,ltr) in memo:
            return memo [(S,ltr)]
        
        if S == "":
            result = ""
        elif S[0] <= ltr:
            result = helper(S[1:], ltr)
        else:
            use = S[0] + helper(S[1:], max(ltr, S[0]))
            lose = helper(S[1:], ltr)
            if len(use) >= len(lose):
                result = use
            else:
                result = lose

        memo [(S,ltr)] = result

        return result


    return helper(S,ltr)
