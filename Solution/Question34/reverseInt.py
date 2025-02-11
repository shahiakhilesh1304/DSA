from Ruler import testCases
from Ruler import util


def reverse(x: int) -> int:
    res, data = 0, abs(x)
    while data:
        val = data%10
        data= data//10
        res = (res*10)+val
        if res > ((2**31) - 1):
            return 0
    if x<0:
        return -res
    return res     
    
if __name__ == "__main__":
    testcases = testCases.get_testcases(__file__)
    analyzer,source = util.start(reverse)
    for input,output in testcases.items():
        file = open(input)
        x = int(file.readline().strip())
        res = reverse(x)
        print(res)
        file.close()
        result = testCases.validator([res],output)
        print(result)
        util.report(analyzer,source,reverse)
        





