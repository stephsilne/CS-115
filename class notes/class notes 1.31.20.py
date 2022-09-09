from cs115 import *

def exclaim (s):
    return s + '!'

def exclaimAll (strs):
    return map (exclaim, strs)

def suffixAll (s, strs):
    
    "adds s at the end of each string in strs"

    return map (makeSuffix(s), strs)


def test ():
    print (suffixAll('!', ['global','warming']) == exclaimAll(['global','warming']))


def makeSuffix (char):

        def suff (s):
            return s + char
        return suff

    
