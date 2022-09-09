from cs115 import*
'''edit distance'''
def ED(first,second):
    if first == '':
        return len(second)
    elif second == '':
        return len(first)
    elif first[0] == second[0]:
        return ED(first[1:],second[1:])
    else:
        substitution = 1 + ED(first[1:],second[1:])
        deletion = 1 + ED(first[1:],second)
        insertion = 1 + ED(first,second[1:])
        return min(substitution,deletion,insertion)
    
def reverse(lst):
    def rev(lst,acc):
        if lst == []:
            return acc
        else:
            return rev(lst[1:],[lst[0]]+acc)
    return rev(lst,[])
