'''
@author:   Stephaan Silne
Pledge:    'I pledge my honor that I have abided by the Stevens Honor System'

CS115 - Lab 5
'''
import time
from cs115 import map

words = []
HITS = 10

def fastED(first, second):
    '''Returns the edit distance between the strings first and second. Uses
    memoization to speed up the process.'''
    memo = {}
    '''defines the dictionary for fastED, where the keys are tuples'''
    def fED(first,second):
        '''defines fED which takes in the same input as fastED which is two words: first and second'''
        if (first,second) in memo:
            '''the case if both words are in memo already'''
            return memo [(first,second)]
            '''returns the tuple that is already contained in the dictionary memo'''
        elif first == '':
            '''otherwise, if the first string given is empty, then the edit distance cant be made'''
            memo [(first,second)] = len(second)
            '''puts the tuple (first,second):len(second) into the dictionary table'''
            return len(second)
            '''returns the length of the second string as the is the only distance able to be given if the other string is empty'''
        elif second == '':
            '''otherwise if the second word given is empty, then the edit distance cannot be made from a string and an empty space'''
            memo [(first,second)] = len(first)
            '''puts the tuple (first,second): len(first) into the dictionary table'''
            return len(first)
            '''returns the length of the first word given as the only distance that can be given and editted is the length of the first string'''
        elif first[0] == second [0]:
            '''otherwise, if the first element of the first word and second word match'''
            memo[(first,second)] = fED(first[1:],second[1:])
            '''saves the tuple (first,second): fED(first[1:],second[1:]) into the dictionary table'''
            return fED(first[1:],second[1:])
            '''recursively returns the edit distance of the rest of the first and second words given'''
        else:
            substitution = 1+ fED(first[1:],second[1:])
            '''evaluates a substitution but getting rid of the first element of both words'''
            deletion = 1 + fED(first[1:], second)
            '''deletes the first element of the first word and evaluated the edit distance of the rest of the word and the second word recursively'''
            insertion = 1 + fED(first,second[1:])
            '''inserts another element and evaluates the first word and the rest of the second word'''
            memo[(first,second)] = min(substitution,deletion,insertion)
            '''inputs the tuple (first,second):min(substitution,deletion,insertion) into the dictionary to future reference'''
            return min(substitution,deletion,insertion)
            '''returns the minimum edit distance of the three evaluations'''
    return fED(first,second)
    '''returns the helper function for fastED that ulilizes memoization'''

def getSuggestions(user_input):
    '''For each word in the global words list, determine the edit distance of
    the user_input and the word. Return a list of tuples containing the
    (edit distance, word).'''
    return map(lambda w: [fastED(user_input,w),w],words[0:])
    '''maps the lambda function with takes as input 'w' and returns a list with the editDistance as the first element and the word in the global dictionary as the second element. This is mapped over the entire global dictionayr given'''
    

def spam():
    '''Main loop for the program that prompts the user for words to check.
    If the spelling is correct, it tells the user so. Otherwise, it provides up
    to HITS suggestions.

    To exit the loop, just hit Enter at the prompt.'''
    while True:
        user_input = input('spell check> ').strip()
        if user_input == '':
            break
        if user_input in words:
            print('Correct')
        else:
            start_time = time.time()
            suggestions = getSuggestions(user_input)
            suggestions.sort()
            endTime = time.time()
            print('Suggested alternatives:')
            for suggestion in suggestions[:HITS]:
                print(' %s' % suggestion[1])
            print('Computation time:', endTime - start_time, 'seconds')
    print('Bye')

if __name__ == '__main__':
    f = open('3esl.txt')
    for word in f:
        words.append(word.strip())
    f.close()
    spam()
