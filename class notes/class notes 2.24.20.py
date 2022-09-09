from cs115 import*

def LCS(S1, S2):
    """Length of longest common subsequence."""
    if S1 == "" or S2 == "": return 0
    elif S1[0] == S2[0]:  
        return 1 + LCS(S1[1:], S2[1:])
    else:
        return max(LCS(S1, S2[1:]), LCS(S1[1:], S2))

    





