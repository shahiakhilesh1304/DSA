from Ruler import testCases
from Ruler import util


def rotationLeft(d,arr):
    i = 0
    while i < d:
        arr.append(arr.pop(0))
        i += 1
    return arr


if __name__ == "__main__":
    testcases = testCases.get_testcases(__file__)
    analyzer,source = util.start(rotationLeft)
    for input,output in testcases.items():
        file = open(input)
        firstline = file.readline().strip().split()
        length = firstline[0]
        d = firstline[1]
        arr = list(map(int,file.readline().strip().split()))
        result = rotationLeft(int(d),arr)
        print(result)
        file.close()
        print(testCases.validator(result,output))
    util.report(analyzer,source,rotationLeft)


