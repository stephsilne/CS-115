'''
fastED from lab5
'''
from cs115 import*

def fastED(first, second):
    '''Returns the edit distance between the strings first and second. Uses
    memoization to speed up the process.'''
    def fastED_help(first, second, memo):
        if (first, second) in memo:
            return memo[(first, second)]
        elif first == '':
            result = len(second)
        elif second == '':
            result = len(first)
        elif first[0] == second[0]:
            result = fastED_help(first[1:], second[1:], memo)
        else:
            substitution = 1 + fastED_help(first[1:], second[1:], memo)
            deletion = 1 + fastED_help(first[1:], second, memo)
            insertion = 1 + fastED_help(first, second[1:], memo)
            result = min(substitution, deletion, insertion)
        memo[(first, second)] = result
        return result    
    return fastED_help(first, second, {})

#TRACER: INCLUDE THE DEPTH PARAMETER IN THE HELPER FUNCTION OF YOUR MAIN CODE; IF THERE IS ALREADY A HELPER FUNCTION, THEN JUST ADD 'DEPTH'


def fastED_tracer(first,second):
    def fED_tracer(first,second,memo,depth):
        print((depth*'  ') + 'fED_tracer(',first,second,')')
        if (first, second) in memo:
            return memo[(first, second)]
        elif first == '':
            result = len(second)
        elif second == '':
            result = len(first)
        elif first[0] == second[0]:
            result = fED_tracer(first[1:], second[1:], memo,depth+1)
        else:
            substitution = 1 + fED_tracer(first[1:], second[1:], memo,depth+1)
            deletion = 1 + fED_tracer(first[1:], second, memo,depth+1)
            insertion = 1 + fED_tracer(first, second[1:], memo, depth+1)
            result = min(substitution, deletion, insertion)
        memo[(first, second)] = result
        return result
    print ('TRACING...')
    return fED_tracer(first, second, {},0)


