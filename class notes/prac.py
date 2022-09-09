from cs115 import*

def len_from_string(num):
    string = str(num)
    if string == []:
        return 0
    else:
        return 1 + len_from_string(string[1:])





def outputprimes(n):
    num = 1
    primes = []
    while n > 0 and num > 0:
        if isprimeornot(num) == True:
            primes += [num]
            n -= 1
        num +=1
    print(primes)
        
def isprimeornot(k):
    m = filter(lambda x: k % x == 0, range(1,k))
    if len(m) == 1:
        return True
    else:
        return False


def hasduplicates(lst):
    blank = []
    for i in range(len(lst)):
        if lst[i] not in blank:
            blank += [lst[i]]
    if len(blank) != len(lst):
        print("yes has dupes")
    else:
        print("No dupes at all")
        
        
        
