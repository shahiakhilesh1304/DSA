from Ruler import testCases
from Ruler import util
from math import ceil


def canJump(nums: list[int]) -> bool:
        reach = 0
        for i ,jump in enumerate(nums):
            if i > reach:
                return False
            reach = max(reach,i+jump)
            if reach == len(nums)-1:
                return True
        return True
    
if __name__ == "__main__":
    testcases = testCases.get_testcases(__file__)
    analyzer,source = util.start(canJump)
    print("=> 0 -> False")
    print("=> 1 -> True")
    for input,output in testcases.items():
        file = open(input)
        prices = list(map(int,file.readline().strip().split()))
        res = canJump(prices)
        print(res)
        file.close()
        res = int(res)
        result = testCases.validator([res],output)
        print(result)
        util.report(analyzer,source,canJump)