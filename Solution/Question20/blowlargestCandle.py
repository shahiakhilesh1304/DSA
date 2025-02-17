from Ruler import testCases
from Ruler import util
import math


def largeCandle(candles):
    maxi = -math.inf
    count = {}
    for candle in candles:
        if maxi < candle:
            maxi=candle
        if candle in count.keys():
            count[candle] = count[candle]+1
        else:
            count[candle] = 1
    return count[maxi]
    
if __name__ == "__main__":
    testcases = testCases.get_testcases(__file__)
    analyzer,source = util.start(largeCandle)
    for input,output in testcases.items():
        file = open(input)
        length = int(file.readline().strip().split()[0])
        candles = list(map(int, file.readline().strip().split()))
        print(candles)
        result = largeCandle(candles)
        print(result)
        file.close()
        result = testCases.validator([result],output)
        print(result,"\n\n")
        util.report(analyzer,source,largeCandle)
