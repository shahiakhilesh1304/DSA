from Ruler import testCases
from Ruler import util
import math


def _gcd(a,b):
    if b==0:
        return a
    else:
        return _gcd(b,a%b)

def lcm(a,b):
    return (a*b)/_gcd(a,b)

def smallest(n):
    res = 1
    for i in range(2,n+1):
        res = int(lcm(res,i))
    return res

    
if __name__ == "__main__":
    testcases = testCases.get_testcases(__file__)
    analyzer,source = util.start(smallest)
    for input,output in testcases.items():
        file = open(input)
        t = int(file.readline().strip().split()[0])
        r = []
        for _ in range(t):
            n = int(file.readline().strip().split()[0])
            # print(n)
            result = smallest(n)
            print(result)
            r.append(result)
        file.close()
        result = testCases.validator(r,output)
        print(result,"\n\n")
        util.report(analyzer,source,smallest)
        



