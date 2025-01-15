
from Ruler import testCases
from Ruler import util


def matchingStrings(stringList, queries):
    result =[]
    for i in queries:
        count = 0
        for j in stringList:
            if i == j:
                count += 1
        result.append(count)
    return result
    
if __name__ == "__main__":
    testcases = testCases.get_testcases(__file__)
    analyzer,source = util.start(matchingStrings)
    for input,output in testcases.items():
        file = open(input)
        StringListSize = int(file.readline().strip().split()[0])
        queries = []
        stringList = []
        for _ in range(StringListSize):
            data = file.readline().strip().split()[0]
            stringList.append(data)
        QueryListSize = int(file.readline().strip().split()[0])
        for _ in range(QueryListSize):
            data = file.readline().strip().split()[0]
            queries.append(data)
        result = matchingStrings(stringList, queries)
        for i in result:
            print(i)
        file.close()
        result = testCases.validator(result,output)
        print(result,"\n\n")
        util.report(analyzer,source,matchingStrings)
        del queries 
        del stringList