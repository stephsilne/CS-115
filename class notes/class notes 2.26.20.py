from cs115 import*

def subset (target,L):

    return subsetT(target,L,0)


def subsetT(target,L,n):
    print (n* '   ', 'subset', target, L)
    if L == []:
        return 0
    elif L[0] > target:
        return subsetT(target, L[1:], n+1)
    else:
        use = L[0] + subsetT(target - L[0], L[1:], n+1)
        lose = subsetT(target, L[1:], n+1)
        return max(use, lose)


assert subset (5, [2,2,7,1]) == 5

