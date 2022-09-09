from cs115 import*

def g(n):
    if n >= 0:
        return n + 0
    else:
        x = -n
        return x

def summ(x,y):
    if x == 0 and y == 0:
        return 0
    elif x == 0:
        return y
    elif y == 0:
        return x
    else:
        return 1 + summ(x-1,y)

def fastLCS_alt(S1,S2):
    memo = {}   
    def fLCS(S1,S2):
        if (S1,S2) in memo:
            return memo[(S1,S2)]
            '''places value in dictionary so we can remember it'''
        elif S1 == '' or S2 == '':
            memo [(S1,S2)] = 0
            return 0
        elif S1[0] == S2[0]:
            answer = 1 + fLCS(S1[1:],S2[1:])
            memo [(S1,S2)] = answer
            return answer
        else:
            chopS1 = fLCS(S1[1:],S2)
            chopS2 = fLCS(S1,S2[1:])
            answer = max(chopS1,chopS2)
            memo [(S1,S2)] = answer
            return answer
        return fLCS(S1,S2)

def collatz(n):
    print(n,end = '')
    if n == 1:
        return
    if n % 2 == 0:
        collatz(n//2)
    else:
        collatz(3*n + 1)

def makeAt(strs):
    if strs == []:
        return []
    else:
        def find_A(W):
            return W[0] == 'a'
        def makeit(S):
            return '@' + S[1:]
    return map(makeit, filter(find_A,strs))
