from Ruler import testCases
from Ruler import util
from math import ceil


def maxProfit(prices: list[int]) -> int:
        max_ = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                max_ += prices[i] - prices[i - 1]
        return max_
    
if __name__ == "__main__":
    testcases = testCases.get_testcases(__file__)
    analyzer,source = util.start(maxProfit)
    for input,output in testcases.items():
        file = open(input)
        prices = list(map(int,file.readline().strip().split()))
        res = maxProfit(prices)
        print(res)
        file.close()
        result = testCases.validator([res],output)
        print(result)
        util.report(analyzer,source,maxProfit)