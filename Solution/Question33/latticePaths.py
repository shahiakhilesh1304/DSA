from Ruler import testCases
from Ruler import util
import math


def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)


def latticePaths(n,m):
    return int((factorial(n+m)/(factorial(n)*factorial(m)))%((10**9)+7))


        
    
if __name__ == "__main__":
    testcases = testCases.get_testcases(__file__)
    analyzer,source = util.start(latticePaths)
    for input,output in testcases.items():
        file = open(input)
        t = int(file.readline().strip())
        res = []
        for _ in range(t):
            n,m = list(map(int,file.readline().strip().split()))
            result = latticePaths(n,m)
            res.append(result)
        print(res)
        file.close()
        result = testCases.validator(res,output)
        print(result,"\n\n")
        util.report(analyzer,source,latticePaths)
        





