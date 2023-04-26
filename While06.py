def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """ 
    i=0
    k=0
    n=len(s)
    while i<n:
        if s[i]=="a":
            k=k+1
        elif s[i]=="u":
            k=k+1
        elif s[i]=="o":
            k=k+1
        elif s[i]=="e":
            k=k+1
        elif s[i]=="i":
            k=k+1
        i=i+1
        
    return n-k
s=str(input())
print(main(s))