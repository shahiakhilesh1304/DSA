m = int(input("Enter the first number: "))
n = int(input("Enter the second number: "))

if m != 0 and n != 0:
    i = 0
    while n != 0:
        i+=1
        r = m % n
        m = n
        n = r
    
    print("GCD is:", m)
    print("Number of iterations:", i)
else:
    print("GCD is undefined for 0")