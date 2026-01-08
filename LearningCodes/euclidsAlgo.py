def gcdv1(m,n):
    if m < n:
        m,n = n,m
    if m == 0 or n == 0:
        return "GCD is undefined for 0"
    if m%n == 0:
        return n
    else:
        deff = m-n
        return gcdv1(max(n,deff),min(n,deff))

def gcdv2(m,n):
    if m < n:
        m,n = n,m
    while m%n != 0:
        diff = m-n
        m,n = max(n,diff), min(n,diff)
    return n
    
    
if __name__ == "__main__":
    m = int(input("Enter the first number: "))
    n = int(input("Enter the second number: "))
    print("GCD V1 is:", gcdv1(m,n))
    print("GCD V2 is:", gcdv2(m,n))