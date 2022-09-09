'''Stephaan Silne'''
'''I pledge my honor that I have abided by the Stevens Honor System'''

from cs115 import*


def knapsack(capacity,itemList):
    '''defines knapsack that takes in capacity and a defined itemList as input'''
    if itemList == [] or capacity == 0:
        '''if the itemList given is empty or the capacity of knapsack is 0'''
        return [0,[]]
        '''return 0 for capacity and an empty list for itemList'''
    elif itemList[0][0] > capacity:
        '''if the first index of the itemList is greater than capacity, ignore'''
        return knapsack(capacity,itemList[1:])
        '''return knapsack recursively to the rest of itemList'''
    else:
        useit = knapsack(capacity - itemList[0][0], itemList[1:])
        '''useit treats knapsack as [greatest-capacity,[accordingitemlist]]; if used, the first index of an element in itemList will be subtracted from capacity'''
        usingit = [useit[0] + itemList[0][1],[itemList[0]] + useit[1]]
        '''usingit applies the conditions of useit, by adding the value as the first element, and the corresponding itemList element as the second element'''
        loseit = knapsack(capacity,itemList[1:])
        '''loseit disregards the first element of itemList, calling knapsack for the rest of the itemList'''
        return max(usingit,loseit)
        '''return the maximum value that the itemList can give'''
    



