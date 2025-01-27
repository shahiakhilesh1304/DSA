from Ruler import testCases
from Ruler import util
import math


def sum_to(mk,limit):
    p = (limit-1)//mk
    return mk*p*(p+1) // 2

def multiples(n):
    multi_3 = sum_to(3,n)
    multi_5 = sum_to(5,n)
    multi_15 = sum_to(15,n)
    return multi_3+multi_5-multi_15

    
if __name__ == "__main__":
    testcases = testCases.get_testcases(__file__)
    analyzer,source = util.start(multiples)
    for input,output in testcases.items():
        file = open(input)
        t = int(file.readline().strip().split()[0])
        r = []
        for _ in range(t):
            n = int(file.readline().strip().split()[0])
            result = multiples(n)
            print(result)
            r.append(result)
        file.close()
        result = testCases.validator(r,output)
        print(result,"\n\n")
        util.report(analyzer,source,multiples)
        
