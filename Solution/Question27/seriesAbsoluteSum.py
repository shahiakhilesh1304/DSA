from Ruler import testCases
from Ruler import util
import math


def sum_of_square(n):
    return (n*(n+1)*((2*n)+1))/6

def square_of_sum(n):
    return math.pow(((n*(n+1))/2),2)

def seriesAbsoluteSum(n):
    a = sum_of_square(n)
    b = square_of_sum(n)
    return int(abs(a-b))
    
if __name__ == "__main__":
    testcases = testCases.get_testcases(__file__)
    analyzer,source = util.start(seriesAbsoluteSum)
    for input,output in testcases.items():
        file = open(input)
        t = int(file.readline().strip().split()[0])
        r = []
        for _ in range(t):
            n = int(file.readline().strip().split()[0])
            result = seriesAbsoluteSum(n)
            print(result)
            r.append(result)
        file.close()
        result = testCases.validator(r,output)
        print(result,"\n\n")
        util.report(analyzer,source,seriesAbsoluteSum)
        



