from Ruler import testCases
from Ruler import util
import math


def consequetive(n,k,num):
    max_prod = -math.inf
    for i in range(n-k):
        digit = list(map(int,num[i:i+k]))
        prod = math.prod(digit)
        if max_prod < prod:
            max_prod = prod
    return max_prod     
        
    
if __name__ == "__main__":
    testcases = testCases.get_testcases(__file__)
    analyzer,source = util.start(consequetive)
    for input,output in testcases.items():
        file = open(input)
        t = int(file.readline().strip().split()[0])
        r = []
        for _ in range(t):
            n,k = list(map(int,file.readline().strip().split(' ')))
            num = file.readline().strip().split(' ')[0]
            result = consequetive(n,k,num)
            print(result)
            r.append(result)
        file.close()
        result = testCases.validator(r,output)
        print(result,"\n\n")
        util.report(analyzer,source,consequetive)
        



