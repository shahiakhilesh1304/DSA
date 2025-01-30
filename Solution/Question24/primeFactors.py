from Ruler import testCases
from Ruler import util
import math

def primeFactor(n):
    while n % 2 == 0:
        max_prime = 2
        n //= 2
        
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            max_prime = i
            n //= i
        
    if n > 2:
        max_prime = n
        
    return max_prime

    
if __name__ == "__main__":
    testcases = testCases.get_testcases(__file__)
    analyzer,source = util.start(primeFactor)
    for input,output in testcases.items():
        file = open(input)
        t = int(file.readline().strip().split()[0])
        r = []
        for _ in range(t):
            n = int(file.readline().strip().split()[0])
            result = primeFactor(n)
            print(result)
            r.append(result)
        file.close()
        result = testCases.validator(r,output)
        print(result,"\n\n")
        util.report(analyzer,source,primeFactor)
        
