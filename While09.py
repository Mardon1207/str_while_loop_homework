def main(s):
    """
    A string of numbers is given. Find the sum of all the digits and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    k=0
    n=len(s)
    while i<n:
        k=k+int(s[i])
        i=i+1
        
    return k
s=str(input())
print(main(s))