from Ruler import testCases
from Ruler import util


def evenFibo(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    a,b=0,1
    result = 0
    while True:
        if a%2 == 0:
            result += a
        a,b=b,a+b
        if a > n:
            return result

    
if __name__ == "__main__":
    testcases = testCases.get_testcases(__file__)
    analyzer,source = util.start(evenFibo)
    for input,output in testcases.items():
        file = open(input)
        t = int(file.readline().strip().split()[0])
        r = []
        for _ in range(t):
            n = int(file.readline().strip().split()[0])
            result = evenFibo(n)
            print(result)
            r.append(result)
        file.close()
        result = testCases.validator(r,output)
        print(result,"\n\n")
        util.report(analyzer,source,evenFibo)
        
