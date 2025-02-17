from Ruler import testCases
from Ruler import util
import math


def birthday(choco_bars,d,m):
    if len(choco_bars) < m:
        return 0
    tot_summers = 0
    for i in range(len(choco_bars)):
        summed = 0
        summed = sum(choco_bars[i:i+m])
        if summed == d:
            tot_summers += 1
    return tot_summers
    
if __name__ == "__main__":
    testcases = testCases.get_testcases(__file__)
    analyzer,source = util.start(birthday)
    for input,output in testcases.items():
        file = open(input)
        length = int(file.readline().strip().split()[0])
        choco_bars = list(map(int, file.readline().strip().split()))
        m,d = set(map(int, file.readline().strip().split()))
        result = birthday(choco_bars,d,m)
        print(result)
        file.close()
        result = testCases.validator([result],output)
        print(result,"\n\n")
        util.report(analyzer,source,birthday)
