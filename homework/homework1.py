from cs115 import *
import math


"'I pledge my honor that I have abided by the Stevens Honor System' Stephaan Silne"



#PROBLEM 1: write a factorial function that takes a positive integer 'n' and returns n!

def mult(x,y):

    times = x * y

    return times
    #"returns the value produced by the 'times' function"

def factorial (n):
    #"defines the factorial function, that will take in an input"
    if n > 0:
    #begin of 'if' statement that evaluates if n is greater than 0
        myrange = range (1,n+1)
    #'myrange' gives the range of numbers from 1 to the n given"
        result = reduce(mult, myrange)
     #the function 'result' will use the reduce operator that will apply the 'mult' to my range"
        return result
    #"'the function will return 'result' if n given is greater than 0 (a positive integer)"
    else:
    #" evaluates if n is a negative integer that is not greater than 0"
        return 'Not a positive integer, sorry.'

    #" returns the string above if n < 0"

    



#PROBLEM 2: write a mean function that takes a list as an input and returns avg

def mean (L):
    #"defines the mean function, that will evauate a list given"

    add = sum(L)
    #"the add function sums all values in the list given"

    length = len(L)
    #"'length' function counts how many values are in the list given"

    avg = add / length

    #"the 'avg' function will divide the sum of the list values by how many values there are"

    return avg
    #"this will return the 'avg' function for the mean function"


#PROBLEM 3: write a function that takes a positive integer 'n' as an input and return T or F depending on if its prime or composite

def prime (n): 
    #"defines the prime function, that will test using (T/F) if a prime number is given


    return (n % 2 != 0 and n % 3 != 0) or n == 2 or n ==3

    # checks if a number is non divisible by 2 & 3, and checks if the number is 2 or 3, thus making it a prime number; will give TRUE if prime

    
    

    



    



