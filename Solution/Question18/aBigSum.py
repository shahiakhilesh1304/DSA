from Ruler import testCases
from Ruler import util



def aBigSum(arr):
    if len(arr) == 0:
        return 0
    return int(arr.pop()) + aBigSum(arr)
    
    
if __name__ == "__main__":
    testcases = testCases.get_testcases(__file__)
    analyzer,source = util.start(aBigSum)
    for input,output in testcases.items():
        file = open(input)
        length = int(file.readline().strip().split()[0])
        arr = file.readline().strip().split()
        result = aBigSum(arr)
        print(result)
        file.close()
        result = testCases.validator([result],output)
        print(result,"\n\n")
        util.report(analyzer,source,aBigSum)
