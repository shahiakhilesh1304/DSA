from Ruler import testCases
from Ruler import util
import math


def pythagorian(n):
    multi = -1
    for i in range(1,(n//3)):
        b = (n*(n-2*i))//(2*(n-i)) # derivation picture is in solution.md
        c = n-i-b
        if i*i+b*b == c*c:
            multi = max(multi, i * b * c)
    return multi   
        
    
if __name__ == "__main__":
    testcases = testCases.get_testcases(__file__)
    analyzer,source = util.start(pythagorian)
    for input,output in testcases.items():
        file = open(input)
        t = int(file.readline().strip().split()[0])
        r = []
        for _ in range(t):
            n = int(file.readline().strip().split()[0])
            result = pythagorian(n)
            print(result)
            r.append(result)
        file.close()
        result = testCases.validator(r,output)
        print(result,"\n\n")
        util.report(analyzer,source,pythagorian)
        



