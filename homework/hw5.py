'''
@author:   Stephaan Silne
Pledge:    "I pledge my honor that I have abided by the Stevens Honor System"

CS115 - Hw 5
'''
import turtle  # Needed for graphics

# Ignore 'Undefined variable from import' errors in Eclipse.

def sv_tree(trunk_length, levels):
    '''defines the function 'sv_tree' which takes as input the length of the trunk (trunk_length) and the number of levels given'''
    if levels == 0:
        '''if the levels given is 0, then a tree cannot be made'''
        turtle.forward(0)
        '''returns the turtle.forward distance of 0, given that 0 levels were given as input'''
        return
        '''empty return so as to not stop the recursive function, but to escape once the case is not applicable'''
    else:
        turtle.forward(trunk_length)
        '''otherwise, move the cursor to the distance of the given trunk_length value'''
        turtle.left(60)
        '''rotate the cursor to the left 60 degree in order to create a smaller branch'''
        sv_tree(trunk_length/2,levels -1)
        '''call the recursive function to create a smaller branch that is the trunk_length divided by 2, continuing a level less than the level given'''
        turtle.right(120)
        '''rotate the cursor to the right 120 degrees or 'another 60 degrees' so as to make another branch'''
        sv_tree(trunk_length/2,levels -1)
        '''recursively call the function to create another branch that is half the length of the original trunk_length, continuing for another level less than the one given'''
        turtle.left(60)
        '''rotate the cursor back to its original heading path'''
        turtle.backward(trunk_length)
        '''move the cursor back to the original position by going backwards the distance of the original trunk_length'''
        return
        '''empty return so as to not halt the recursive function, but to escape once completed'''

def fast_lucas(n):
    '''defines 'fast_lucas' which takes as input 'n' and returns the nth Lucas number using the memoization technique
    shown in class and lab. The Lucas numbers are as follows:
    [2, 1, 3, 4, 7, 11, ...]'''
    def f_lucas(n,memo):
        '''defines the helper function 'f_lucas' which takes in as input the nth Lucas number and memo for memoization'''
        if (n) in memo:
            '''the case if the tuple of the value n is already within the memo dictionary'''
            return memo[(n)]
            '''returns the tuple of the nth Lucas number if already contained within the dictionary'''
        elif n == 0:
            '''otherwise if the n value given is 0'''
            result = 2
            '''the nth Lucas number should result to be 2, which will be 'returned' by the case if true'''
        elif n == 1:
            '''otherwise if n value given is 1'''
            result = 1
            '''the 'returned' result should equal to 1'''
        else:
            result = f_lucas(n-2,memo) + f_lucas(n-1,memo)
            '''if the other cases do not apply, return the recursive function 'f_lucas' of the value of n-1 plus the 'f_lucas' of value n-2, essentially returning the sum of the two previous numbers in the Lucas number domain'''
        memo[(n)] = result
        '''defines result or all the 'return' statements as tuples within the memo dictionary'''
        return result
        '''returns result which equals all the return values of all cases within the recursive function'''
    return f_lucas(n,{})
    '''returns the call upon the recursive function 'f_lucas' which takes as input n and {}, which establishes the memo dictionary'''
        

def fast_change(amount,coins):
    '''Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.'''
    def fast_change_helper(amount,coins, memo):
        '''defines fast_change_helper which takes as input the amount given, the list of coins (tuple) and memo for memoization of returns'''
        if (amount,coins) in memo:
            '''if the tuple of the amount and the corresponding number of coins is in the memo dictionary'''
            return memo[(amount,coins)]
            '''return the index which contains this tuple within memo'''
        elif coins == [] or amount == 0:
            '''if the list of coins given is empty of the amount given is 0'''
            result = 0
            '''return 0 as 0 coins can be made from an amount equaling 0'''
        elif coins == ():
            '''otherwise if coins is an empty tuple'''
            result = float("inf")
            '''return 'float("inf") as infinetly many coins can be made from no designated coin values'''
        elif amount < coins[0]:
            '''otherwise if the first element of coins is larger than the amount given'''
            result = fast_change_helper(amount,coins[1:],memo)
            '''return the recursive function to the rest of the list, as the coin denomination cannot be used'''
        else:
            useit = 1 + fast_change_helper(amount-coins[0],coins[0:],memo)
            '''defines useit which returns 1 plus the recursive call of the given amount minus the first coin denomination, as it is being used once, to the whole list again'''
            loseit = fast_change_helper(amount,coins[1:],memo)
            '''defines loseit which ignores the first coin denomination in the list given as it cannot be used, recursively applying fast_change_helper to the rest of the list'''
            result = min(useit,loseit)
            '''returns the minimum amount of coins between useit and loseit that can be made from the amount given'''
        memo[(amount,coins)] = result
        '''memoizes result which is the 'return statements' of all the cases for the recursive function'''
        return result
        '''returns result which is the 'return statements' of all cases for the recursive function'''
    return fast_change_helper(amount, tuple(coins), {})
    '''returns the call upon the recursive function 'fast_change_helper' which takes in the amount given, tuples the coins list, and establishes the dictionary by whihc memo will fill'''

# If you did this correctly, the results should be nearly instantaneous.
print(fast_lucas(3))  # 4
print(fast_lucas(5))  # 11
print(fast_lucas(9))  # 76
print(fast_lucas(24))  # 103682
print(fast_lucas(40))  # 228826127
print(fast_lucas(50))  # 28143753123

print(fast_change(131, [1, 5, 10, 20, 50, 100]))
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(673, [1, 5, 10, 20, 50, 100]))
print(fast_change(724, [1, 5, 10, 20, 50, 100]))
print(fast_change(888, [1, 5, 10, 20, 50, 100]))

# Should take a few seconds to draw a tree.
sv_tree(100, 4)
