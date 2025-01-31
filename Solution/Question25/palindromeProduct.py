from Ruler import testCases
from Ruler import util
import math


def checkPlndrm(num):
    return str(num) == str(num)[::-1]

def palindrome():
    res = []
    for i in range(100000,(999*999)+1):
        if checkPlndrm(i):
            res.append(i)
    return res

def checkSum(n):
    def product3_Sum(num):
        for i in range(100,1000):
            # print(num)
            # print(i)
            if num%i ==0 and num//i>=100  and num//i<=999:
                return True
        return False
    for i in palindrome[::-1]:
        # print(i)
        if product3_Sum(i) and i <n:
            return i

    
if __name__ == "__main__":
    testcases = testCases.get_testcases(__file__)
    analyzer,source = util.start(checkSum)
    palindrome = palindrome()
    for input,output in testcases.items():
        file = open(input)
        t = int(file.readline().strip().split()[0])
        r = []
        for _ in range(t):
            n = int(file.readline().strip().split()[0])
            # print(n)
            result = checkSum(n)
            print(result)
            r.append(result)
        file.close()
        result = testCases.validator(r,output)
        print(result,"\n\n")
        util.report(analyzer,source,checkSum)
        



