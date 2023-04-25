def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd digits.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    k=0
    n=len(s)
    while i<n:
        if int(s[i])%2==1:
            k=k+int(s[i])
        i=i+1
        
    return k
s=str(input())
print(main(s))