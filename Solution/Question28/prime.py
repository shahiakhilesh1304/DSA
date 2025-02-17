from Ruler import testCases
from Ruler import util
import math


def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True
    
def primeDict():
    primes = []
    for i in range(2,1000000):
        if isPrime(i):
            primes.append(i)
    return primes
        
    
if __name__ == "__main__":
    testcases = testCases.get_testcases(__file__)
    analyzer,source = util.start(primeDict)
    primes = primeDict()
    for input,output in testcases.items():
        file = open(input)
        t = int(file.readline().strip().split()[0])
        r = []
        for _ in range(t):
            n = int(file.readline().strip().split()[0])
            result = primes[n-1]
            print(result)
            r.append(result)
        file.close()
        result = testCases.validator(r,output)
        print(result,"\n\n")
        util.report(analyzer,source,primeDict)
        



