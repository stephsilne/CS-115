'''
@author: Stephaan Silne
Pledge: 'I pledge my honor that I have abided by the Stevens Honor System'

CS115 - Hw 9

Objective: To become familiar with imperative style and for and while loops.

Instructions: Submit a copy of this file (with your name and pledge and) with
the incomplete functions completed. Don't change the functions that are
already implemented.

# Search for "TODO" to find the incomplete functions.
'''
from cs115 import map, reduce

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Exercise 1
' Study function questify(). Then implement questifyAlt() so that it gives
' the same results as questify(), using map and lambda but no helping function.
' Hint: adapt the body of addQuestmark().
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def questify(str_list):
    '''Assume str_list is a list of strings. Returns a list of
    the same strings but with ? suffixed to each.'''
    def addQuestmark(s):
        '''Adds a question mark to a string.'''
        return s + '?'

    return map(addQuestmark, str_list)

def questifyAlt(str_list):
    '''Same as questify'''
    return map(lambda w: w + '?', str_list)
    '''returns the mapping anonymous function lambda to every string in the list'''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Exercise 2
' Study functions leppard() and catenate(). Implement catenateLoop(), without
' using recursion or reduce or any built-in Python function. Instead, use a
' loop. In some ways your code will resemble the body of leppard().
' If you prefer, you can follow the style of leppardIndex(), but I suggest not.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def leppard(inputString):
    '''Mystery.'''
    outputString = ''
    for symbol in inputString:
        if symbol == 'o':
            outputString = outputString + 'ooo'
        else:
            outputString = outputString + symbol
    print(outputString)

def leppardIndex(inputString):
    '''Same as leppard(), but using an integer index rather than directly
    referring to elements of the input string.'''
    outputString = ''
    for i in range(len(inputString)):
        if inputString[i] == 'o':
            outputString = outputString + 'ooo'
        else:
            outputString = outputString + inputString[i]
    print(outputString)

def catenate(str_list):
    '''Assume str_list is a list of strings.
    Return a single string, their catenation.'''
    if str_list == []:
        return ''
    return reduce(lambda s, t: s + t, str_list)

def catenateLoop(str_list):
    '''Same as catenate'''
    catenation = ''
    '''initializes the variable catenation as an empty string'''
    for element in str_list:
        '''for every element is the list of strings'''
        if len(str_list) >= 1:
            '''if the length of the list given is greater than or equal to 1'''
            catenation = catenation + element
            '''update catenation by adding each iterated element to it, thus making a single string of all elements added together when loop is finished'''
        else:
            catenation = catenation + ''
            '''if given an empty string, catenation should just continue to be an empty string'''
    return catenation
    '''once all iterations are completed by the for loop, return the final catenation'''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Exercise 3
' Implement letterScoreLoop using --you guessed it-- a loop instead of
' recursion. Also, do not use map or reduce.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
scrabbleScores = [["a", 1], ["b", 3], ["c", 3], ["d", 2], ["e", 1], ["f", 4], \
                  ["g", 2], ["h", 4], ["i", 1], ["j", 8], ["k", 5], ["l", 1], \
                  ["m", 3], ["n", 1], ["o", 1], ["p", 3], ["q", 10], ["r", 1], \
                  ["s", 1], ["t", 1], ["u", 1], ["v", 4], ["w", 4], ["x", 8], \
                  ["y", 4], ["z", 10]]

aDictionary = ["a", "am", "at", "apple", "bat", "bar", "babble", "can", "foo", \
               "spam", "spammy", "zzyzva"]

def letterScore(letter, scorelist):
    '''Assume scorelist is a list of lists [ltr, val] where ltr is a single
    letter and val is a natural number. Assume letter is a single letter string,
    that occurs in scorelist. Return the associated value.'''
    if letter == scorelist[0][0]:
        return scorelist[0][1]
    return letterScore(letter, scorelist[1:])

def letterScoreLoop(letter, scorelist):
    '''Same as letterScore'''
    score = 0
    '''initializes variable score to 0 which will be manipulated in the for loop'''
    for ltr in scorelist:
        '''for every element in the scorelist given'''
        if ltr[0] == letter:
            '''if the first element (letter) equals the letter given'''
            score = score + ltr[1]
            '''update score by adding the second element of ltr to score'''
    return score
    '''return the final score, once all iterations are complete'''
            
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Exercise 4
' Implement wordScoreLoop using a loop instead of recursion. (And don't
' use map or reduce.)
' Use letterScore() or letterScoreLoop(); it shouldn't matter which one.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def wordScore(S, scorelist):
    '''Assume S is a string and scorelist is in the format above and
    includes every letter in S. Return the scrabble score of that string.'''
    if S == '':
        return 0
    return letterScore(S[0], scorelist) + wordScore(S[1:], scorelist)

def wordScoreLoop(S, scorelist):
    '''Same as wordScore'''
    val = 0
    '''initializes the variable 'val' to equal 0, whcih will be manipulated in the for loop'''
    for char in S:
        '''for every character (char) in the string S given'''
        val = val + letterScore(char,scorelist)
        '''update val by adding the letterScore to each char in S using the function'''
    return val
    '''return the final val once all iterations are complete'''
        

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Exercise 5
' Implement wordsWithScoreLambda using a lambda instead of the helper scoreWord.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def wordsWithScore(dct, scores):
    '''Assume dct is a list of words and scores is a list of [letter, number]
    pairs. Return a copy of the dictionary, annotated so each word is paired
    with its value. For example, wordsWithScore(scrabbleScores, aDictionary)
    should return [["a", 1], ["am", 4], ["at", 2] ...etc... ]'''
    def scoreWord(wrd):
        return [ wrd, wordScore(wrd, scores) ]

    return map(scoreWord, dct)

def wordsWithScoreLambda(dct, scores):
    '''Same as wordsWithScore'''
    return map(lambda wrd: [wrd,wordScore(wrd,scores)],dct)
    '''map the anonymous function that takes a word and returns wordScore(wrd,scores) to each word in dct'''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Exercise 6
' Implement wordsWithScoreLoop using a loop instead of map or recursion.
' Be careful NOT to change the dictionary.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def wordsWithScoreLoop(dct, scores):
    '''Same as wordsWithScore'''
    wrd = []
    '''initializes wrd to be an empty list that will be manipulated in the for loop'''
    for elem in dct:
        '''for every element in dct given'''
        wrd = wrd + [[elem, wordScore(elem,scores)]]
        '''update wrd by adding [[elem, wordScore(elem,scores)]] to it for every elem'''
    return wrd
    '''returns the final wordsWithScore list for all iterating elements in dct'''
