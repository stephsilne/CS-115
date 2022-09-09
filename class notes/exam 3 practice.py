from cs115 import*

vowels = ['a','e','i','o','u']
def spamify(word):
    p = []
    for i in range(len(word)):
        if word[i] not in vowels:
            p += [word[0:i] + 'spam' + word[i+1:]]
    return p


def mapSqr(L):
    newL = []
    for ele in L:
        newL += [ele**2]
    return newL


def f(L):
    newLIST = map(lambda x: x,L)
    i = 1
    while i < len(newLIST)-1:
        newLIST[i] = (newLIST[i] + newLIST[i+1] + newLIST[i-1])/3
        i += 1
    return newLIST
        
                 
class Point:
    def __init__(self,InputX, InputY):
        self.x = InputX
        self.y = InputY

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    
def factorial (N):
    num = 1
    for i in range(1,N+1):
        num *= i
    return num

def likesAretha(artistList):
    artst = 0
    for i in artistList:
        if i == 'Aretha Franklin':
            artst += 1
    if artst > 0:
        return True
    return False

def likesaretha(artistList):
    j = 0
    while j < len(artistList):
        if artistList[j] != 'Aretha Franklin':
            j += 1
        elif artistList[j] == 'Aretha Franklin':
            return True
    return False
        

def rotateLeft(element,k):
    for i in range(k):
        element[i-k] = element[i]
    return element
    

    

def myquestify(slist):
    lists = []
    for ele in slist:
        lists += [ele + '?']
    return lists


def mycatenate(strlist):
    lists = ''
    for ele in strlist:
        lists += ele
    return lists



def numMatches ( L1 , L2 ):
    i = 0
    j = 0
    matches = 0
    print(i,j,matches)
    while i < len( L1 ) and j < len( L2 ):
        if L1 [ i ] == L2 [ j ]:
            matches += 1
            i += 1
            j += 1
        elif L1 [ i ] < L2 [ j ]:
            i += 1
        else:
            j += 1
        print(i,j,matches)
    return matches


def isitprime(n):
    val = 0
    for i in range(1,n+1):
        if n % i == 0:
            val += i
    return val == n+1


def prime(num):
    possdivs = range(1,num)
    divs = filter(lambda num,k: num % k == 0,possdivs)
    return len(divs) == 1



















    
    
    
