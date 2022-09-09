"""Stephaan Silne"""
"""I pledge my honor that I have abided by the Stevens Honor System"""
"""1.30.20"""

from cs115 import *
import math


def inverse (n):

    "defines the inverse function"

    input = 1/n

    "divides 1 by the input n given to calculate inverse of number"
    
    return input

    "returns the inverse/reciprocal"





def e(n):

    "defines the 'e' function"

    myrange = range (0, n+1)

    "'myrange' is a function that displays a range of numbers from 1 to n"
    
    map1 = map ( fctrl, myrange)

    "'map1' is a map function that will utilize the factorial function defined below and apply it to the 'myrange'"

    map2 = map (inverse, map1)

    "'map2' is a map function that takes the inverse of all the 'factorialed' range of numbers and using the inverse function, returns the reciprocals"

    taylor = sum (map2)

    "'taylor' is a function that will sum up all the inverse factorial range of values to n from map2"

    return taylor

    "this will return the approximated e values adding up to the first n terms of the sequence"

def fctrl (n):
    "defines the factorial function that will be used above"
    
    return math.factorial (n)

    "returns the factorials of the range of numbers from 1 to n given"




def error (n):
    "defines the error function"

    diff = (math.e - e(n))
    "calulates the difference of math.e (ACTUAL VALUE OF e) and the approx. of e given the function e(n) provided above"

    value = abs(diff)
    "'value' will take the absolute value of this difference"


    return value
    "returns the absolute value of difference of e and the approximation"
