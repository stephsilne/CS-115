from cs115 import*



def isPrime(n):
    if not n:
        return 'Error'
    return len(divisors(n)) == 0

def divisors(n):
    divid = range(2,n)
    return filter(lambda m: n%m == 0,divid)


def sieve(L):
    def tracer (L,depth):
        print ((depth *' ') + 'tracer (',L,')')
        if L == []:
            return []
        else:
            return [L[0]] + tracer((filter(lambda X: X % L[0] != 0, L[1:])),depth+1)
    print('tracing....')
    return tracer(L,0)
'''always replace the function call with 'tracer' helper function when tracing'''

def listofPrimes(L):
    def tracer(L,depth):
        print((depth*'') + 'tracer(',L,')')
        if L == []:
            return []
        else:
            return filter(isPrime,L)
    print('tracing....')
    return tracer(L,0)


def reverser(L):
    if L == []:
        return []
    else:
        return reverse(L[1:]) + [L[0]]

def piglatin(s):
    if s == '':
        return ''
    else:
        return s[1:] + s[0] + 'ay'


def getAllSubsets(lst):
    def tracer(lst,depth):
        print ((depth * ' ') + 'tracer (',lst,')')
        if not lst:
            return [[]]
        withFirst = [ [lst[0]] + rest for rest in tracer(lst[1:],depth+1) ]
        withoutFirst = tracer(lst[1:],depth+1)
        return withFirst + withoutFirst
    print ('im tracing dude.........')
    return tracer(lst,0)



def allSubsets(lst):
    if not lst:
        return [[]]
    else:
        withFirst = [[lst[0]] + rest for rest in allSubsets(lst[1:])]
        withoutFirst = allSubsets(lst[1:])
        return withFirst + withoutFirst



def ranger(n):
    return range(1,n)

def mult(m,n):
    if n == 0:
        return 0
    else:
        return m + mult(m,n-1)

def log2(n):
    if n <= 1:
        return 0
    else:
        return 1 + log2(n/2)

def mymap(f,L):
    if L == []:
        return []
    else:
        return [f(L[0])] + mymap(f,L[1:])

def knapsack(capacity,List):
    if List == [] or capacity == 0:
        return [0,[]]
    elif List[0][0] < capacity:
        return knapsack(capacity,List[1:])
    else:
        useit = knapsack(capacity - List[0][0], List[1:])
        usingit = [useit[0] + List[0][1], useit[1] + [itemList[0]]]
        loseit = knapsack(capacity,List[1:])
        return max(usingit,loseit)


def index_of_last_even(L):
    if L == []:
        return -1
    if L[-1] % 2 == 0:
        return len(L)-1
    else:
        return index_of_last_even(L[:-1])

##
##def coin_row_with_values(lst):
##    if lst == []:
##        return [0,[]]
##    use_it = coin_row_with_values(lst[2:])
##    lose_it = coin_row_with_values(lst[1:])
##    new_sum = use_it[0] + lst[0]
##    if new_sum > lose_it[0]:
##        return [new_sum,[lst[0]+use_it[1]]
##    return lose_it

def fib(n):
    def fib_memo(n, memo,depth):
        print((depth * '') + 'fib_memo (',n,memo,')')
        if n in memo:
            return memo[n]
        if n <= 1:
            result = n
        else:
            result = fib_memo(n-1, memo,depth+1) + fib_memo(n-2, memo,depth+1)
        memo[n] = result
        return result
    print('tracinggggggggg')
    return fib_memo(n,{},0)

def farthest_from(L,target):
    def farthest_helper(L,farthest):
        if L == []:
            return 0
        if abs(L[0] - target) > abs(farthest-target):
            return farthest_helper(L[1:],L[0])
        return farthest_helper(L[1:],farthest)
    return farthest_helper(L[1:],L[0])

def seq(n):
    def seq_memo(n, memo,depth):
        print((depth * ' ') + 'seq_memo (',n,memo,')')
        if n in memo:
            return memo[n]
        if n <= 3:
            result = n
        else:
            result = seq_memo(n - 2, memo,depth+1) + seq_memo(n - 3, memo,depth+1)
            memo[n] = result
        return result
    return seq_memo(n, {},0)

def give_change(amount,coins):
    if amount <= 0:
        return (0,[])
    if coins == []:
        return (float('inf'),[])
    lose_it = give_change(amount,coins[1:])
    if coins[0] > amount:
        return lose_it
    use_it = give_change(amount - coins[0],coins)
    num_coins = 1 + use_it[0]
    if lose_it[0] < num_coins:
        return lose_it
    return (num_coins, use_it[1] + [coins[0]])

def fib(n):
    def fib_h(n,memo):
        if n in memo:
            return memo[(n)]
        if n <= 1:
            result = n
        else:
            result = fib_h(n-1,memo) + fib_h(n-2,memo)
        return result
    return fib_h(n,{})

def subset(capacity,items):
    if capacity == 0 or items == []:
        return 0
    if items[0] > capacity:
        return subset(capacity,items[1:])
    use_it = items[0] + subset(capacity - items[0],items[1:])
    lose_it = subset(capacity,items[1:])
    return max(use_it,lose_it)

def span(lst):
    def span_helper(lst,min_value,max_value):
        if lst == []:
            return max_value - min_value
        if min_value > lst[0]:
            return span_helper(lst[1:],lst[0],max_value)
        return span_helper(lst[1:],min_value,lst[0])
    return span_helper(lst[1:],lst[0],lst[0])

def length(lst):
    if lst == []:
        return 0
    else:
        return 1 + length(lst[1:])

car = {"brand": "Ford", "model": "Mustang","year": 1964, "price": 16000}

x = car.get("price", 15000)

print(x)

