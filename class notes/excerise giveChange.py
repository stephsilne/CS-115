'''Stephaan Silne'''
'''I pledge my honor that I have abided by the Stevens Honor System'''

from cs115 import *

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
        '''useit evaluates that a coin will be used by subtracting the amount by the first element usable and then recursively calling itself, returning the numberofcoins as the first element and the listofcoins as a second element''' 
        usingit = [useit[0] + 1, useit[1] + [coins[0]]]
        '''usingit returns a list; it adds 1 to the numberofcoins and then adds the actual coin value to listofcoins in a nested list''' 
        loseit = giveChange(amount,coins[1:])
        '''loseit evaluates giveChange for the rest of the list if the first element in coins is ignorable'''
        return min (usingit,loseit)
        '''returns the minimum of usingit and loseit, by evaluating each list and its elements for the smallest value, being the first element in this case'''




