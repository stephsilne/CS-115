'''
@author:   Stephaan Silne
Pledge:    "I pledge my honor that I have abided by the Stevens Honor System"

CS115 - Hw 2
'''

import sys
from cs115 import map, reduce, filter
# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

def letterScore (letter,scorelist):
    '''defines letterScore which takes in a letter and scorelist as input'''
    if letter == '':
        '''if given letter is an empty string, return 0'''
        return 0
        '''returns 0 upon the if statement'''
    elif letter == scorelist[0][0]:
        '''otherwise if the letter is for instance 'a', return '1'''
        return scorelist[0][1]
        '''returns the value that corresponds to the letter'''
    else:
        return letterScore (letter, scorelist[1:])
        '''returns the letterscore using the scorelist from index 1 onward, if 'a' isn't the letter given'''

def wordScore (S, scorelist):
    '''defines wordScore which takes in a word and scorelist as input'''
    if S == '':
        '''if word is an empty string, return 0'''
        return 0
        '''returns 0 if if statement is true'''
    else:
        return letterScore (S[0], scorelist) + wordScore(S[1:],scorelist)
        '''returns the letterScore of the first character of word, and then recursively does so for the rest of the string'''

def removeOne (e,L):
    '''defines removeOne, which takes in a character 'e' and a list'''
    if L == []:
        '''if the list given is empty, return an empty list'''
        return []
        '''returns empty list given that the if statement is true'''
    elif L[0] == e:
        '''otherwise if the first element of the list is e'''
        return L[1:]
        '''return the rest of the list, excluding 'e', thus removing it from the list'''
    else:
        return [L[0]] + removeOne(e,L[1:])
        '''if cases are false, keep the first element and then apply removeOne to the rest of the list to find 'e'''
    
def find (Rack):
    '''takes a rack, and returns all the word in the dictionary
    that the rack can make'''    
    return filter(lambda x: isWordInRack(x,Rack), Dictionary)
    '''filters through every word in Dictionary, which is taken in as x, and applies 'isWordInRack' to each word'''

def isWordInRack(word,Rack):
    '''returns whether the string word can be made from the list of
    strings rack'''
    if word == '':
        '''if the word given is an empty string, then it is True'''
        return True
        '''returns Boolean value'''
    elif word[0] in Rack:
        '''otherwise if the first character in the word is in Rack'''
        return isWordInRack(word[1:],removeOne(word[0],Rack))
        '''apply 'isWordinRack' to the rest of the word,while also using removeOne to get rid of the first character (only once) that was in both Rack and the word'''
    else:
        return False
        '''if those cases do not work, return False'''
def scoreList(Rack):
    '''defines scoreList, which takes in Rack to give the word in Rack, along with the score'''
    matchScore = map (match, find(Rack))
    '''applies the match function to the words from Dict. in Rack, outputing list of the word and the matching score'''
    return matchScore
    '''returns a list of lists with the word and corresponding score in Rack'''

def match (W):
    '''defines 'match' which takes a word as an input'''
    return [W, wordScore(W,scrabbleScores)]
    '''returns the word, and the corresponding wordScore, using the scrabbleScore list'''

def bestWord(Rack):
    '''defines 'bestWord', which takes in Rack as an input'''
    if scoreList(Rack) == []:
        '''if the scoreList produces and empty list'''
        return ['',0]
        '''return an empty string and the corresponding score of 0'''
    return mxm(scoreList(Rack))
    '''applies the maximum function to the scoreList of words in Rack'''

def mxm(f):
    '''defines mxm which takes in a list'''
    if f == []:
        '''if the list is empty'''
        return []
        '''return an empty list, if the previous if statement is true'''
    elif length(f) == 1:
        '''otherwise if the length of the list is 1, return the only item in the list given it is the maximum'''
        return f[0]
        '''returns the first element of the list, which is the only element (max)'''
    elif f[0][1]< mxm(f[1:])[1]:
        '''otherwise if the second element of the first element (wordScore) is less than the maximum (same element) of the rest of the list'''
        return mxm(f[1:])
        '''return the maximum recursively of the rest of the list'''
    else:
        return f[0]
        '''if those cases do not work, return the first element, as it is the max.'''

def length (M):
    '''defines 'length' which takes a list as an input'''
    if M == []:
        '''if the list is empty, return 0 for length'''
        return 0
        '''returns 0, if the 'if' statement is True'''
    else:
        return 1 + length(M[1:])
        '''otherwise, return 1 + whatever the length of the rest of the list is'''


