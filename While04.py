def main(s):
    """
    A variable of type str is given. Find how many uppercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    k=0
    n=len(s)
    while i<n:
        if s[i].isupper():
            k=k+1
        i=i+1
        
    return k
s=str(input())
print(main(s))