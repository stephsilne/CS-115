'''Stephaan Silne'''
'''I pledge my honor that I have abided by the Stevens Honor System'''


from cs115 import *

def change (amount, coins):
    '''defines change which takes in an amount and the value of each coin available'''
    if coins == [] and amount == 0:
        '''if coins is an empty list and the amount 0, it returns 0 as 0 can be made from 0 coins'''
        return 0
        '''returns 0 if the if statement is true'''
    elif coins == []:
        '''otherwise, if coins ends up resulting to an empty list, return infinity, as however many coinscan be made to support the amount given'''
        return float ("inf")
        '''returns infinity'''
    elif amount < coins[0]:
        '''otherwise if amount is less than the first element of coins'''
        return change(amount, coins[1:])
        '''ignore that first element, and recursively call the function ot the rest of the list'''
    else:
        useit = 1 + change((amount - coins[0]), coins[0:])
        ''''useit' recursively calls 'change', adding 1 for every coin taken and then subtracting this value from amount and computing 'change over the list again as to either use the same coin or another'''
        loseit = change(amount, coins[1:])
        ''''loseit' recursively calls the function when the first element is to be ignored, thus 'losing it'''
        return min (useit,loseit)
        '''returns the minimum number of coins that could be used to add up to amount'''
                    
                      

    

    


