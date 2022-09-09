from cs115 import*
import sys

def traceit(frame, event, arg):
    if event == "call":
        co = frame.f_code
        func_name = co.co_name
        print("event:", event,"of function",func_name)
    return traceit


def pascal_row(n):
    if n < 0:
        return []
    elif n == 0:
        return [1]
    else:
        return [1] + pas_cal(pascal_row(n-1)) + [1]
    

def pas_cal(A) :
    if length(A) == 1:
        return []
    else :
        return [(A[0]+A[1])] + pas_cal(A[1:])

def length(M):
    if M == []:
        return 0
    else:
        return 1 + length(M[1:])



sys.settrace(traceit)
pascal_row(2)
