'''
@author:   Stephaan Silne
Pledge:    "I pledge my honor that I have abided by the Stevens Honor System"

CS115 - Hw 3
'''
from cs115 import *

#PROBLEM 0
def giveChange (amount, coins):
    '''defines 'giveChange' which takes as input an amount and a list of values called 'coins'''
    if coins == [] and amount == 0:
        '''if coins is an empty list and the amount 0, it returns 0 and an empty list, as 0 can be made from 0 coins'''
        return [0,[]]
        '''returns a list of 0 as 'NumberofCoins' and an empty list to represent 'ListofCoins'''
    elif coins == []:
        '''otherwise, if coins ends up resulting to an empty list, return infinity and an empty list, as however many coins can be made to support the amount given'''
        return [float("inf"),[]]
        '''returns a list of infinity as the first element 'NumberofCoins' and an empty list as 'listOfCoins'''    
    elif amount < coins[0]:
        '''otherwise if amount is less than the first element of coins'''
        return giveChange(amount,coins[1:])
        '''ignore that first element, and recursively call the function to the rest of the list'''      
    else:
        useit = giveChange((amount-coins[0]),coins[0:])
        '''useit evaluates that a coin will be used by subtracting the amount by the first element usable and then recursively calling itself, treating the numberofcoins as the first element and the listofcoins as a second element''' 
        usingit = [useit[0] + 1, useit[1] + [coins[0]]]
        '''usingit returns a list; it adds 1 to the numberofcoins and then adds the actual coin value to listofcoins in a nested list''' 
        loseit = giveChange(amount,coins[1:])
        '''loseit evaluates giveChange for the rest of the list if the first element in coins is ignorable'''
        return min (usingit,loseit)
        '''returns the minimum of usingit and loseit, by evaluating each list and its elements for the smallest value, being the first element in this case'''
        
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

# PROBLEM 1
def wordsWithScore(dct, scores):
    '''defines wordsWithScore which takes in a large list of words 'dct' and scores as input'''
    if dct == [] and scores == []:
        '''if dct and scores are both empty list, scores cannot be applied to each word, thus returning an empty list'''
        return []
        '''returns an empty list'''
    else:
        return map(match,dct[0:])
        '''returns the match function mapped over 'dct', giving the word and the score for each word in a list'''
        
def match (S):
    '''defines 'match' which takes in a word as input'''
    if S == '':
        '''if an empty string is given, a score cannot be given'''
        return ['', 0]
        '''returns the empty string and the corresponding score of 0 in a list'''
    else:
        return [S,wordScore(S,scrabbleScores)]
        '''returns a list with the word and the wordScore function applied to the word'''

def wordScore (S, scores):
    '''defines wordScore which takes in a word and score as input'''
    if S == '':
        '''if word is an empty string, return 0'''
        return 0
        '''returns 0 if if statement is true'''
    else:
        return letterScore (S[0], scores) + wordScore(S[1:],scores)
        '''returns the letterScore of the first character of word, and then recursively does so for the rest of the string'''
    
def letterScore (letter,scores):
    '''defines letterScore which takes in a letter and scores as input'''
    if letter == '':
        '''if given letter is an empty string, return 0'''
        return 0
        '''returns 0 upon the if statement'''
    elif letter == scores[0][0]:
        '''otherwise if the letter is for instance 'a', return '1'''
        return scores[0][1]
        '''returns the value that corresponds to the letter'''
    else:
        return letterScore (letter, scores[1:])
        '''returns the letterscore using the scores from index 1 onward, if 'a' isn't the letter given'''   

#PROBLEM 2        
def take(n, L):
    '''take takes in input a number 'n' and a list 'L' to return an index from L[0:n]'''
    if L == []:
        '''if an empty list is given, the take function should not work, returning an empty list'''
        return []
        '''returns an empty list'''
    elif n == 0:
        '''if n given is 0'''
        return []
        '''if the elif statement is true, then take should return an empty list'''
    else:
        return [L[0]] + take(n-1,L[1:])
        '''otherwise return the first element of the list, and then return the 'n-1' of the list from the first index onward'''

#PROBLEM 3
def drop(n, L):
    '''drop takes in input a number 'n' and a list 'L' to return L[n:]'''
    if L == []:
        '''if an empty list is given, then the function cannot return an indexed list, thus returning an empty list'''
        return []
        '''returns an empty list'''
    elif n == 0:
        '''otherwise is number 'n' is 0, it should just return the whole list'''
        return L
        '''returns the entire list given'''
    else:
        return drop(n-1,L[1:])
        '''returns 'n-1' of the list, dropping the first element'''
















