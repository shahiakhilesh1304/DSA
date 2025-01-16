
from Ruler import testCases
from Ruler import util


def arrayManipulated(n, queries):
    data  = [0]*n
    for query in queries:
        a = int(query[0])
        b = int(query[1])
        val = int(query[2])
        data[a-1] = data[a-1]+val
        if b < n:
            data[b] = data[b]-val
    
    result = [0,0]
    for i in data:
        result[0] = result[0]+i
        result[1] = max(result)
    return result[1]    
    
if __name__ == "__main__":
    testcases = testCases.get_testcases(__file__)
    analyzer,source = util.start(arrayManipulated)
    for input,output in testcases.items():
        file = open(input)
        firstLineInput = file.readline().strip().split()
        n = int(firstLineInput[0])
        m = int(firstLineInput[1])
        queries = []
        for _ in range(m):
            queries.append(file.readline().strip().split())
        result = [arrayManipulated(n, queries)]
        for i in result:
            print(i)
        file.close()
        result = testCases.validator(result,output)
        print(result,"\n\n")
        util.report(analyzer,source,arrayManipulated)
        del queries 