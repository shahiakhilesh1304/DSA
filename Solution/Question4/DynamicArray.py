from Ruler import util

def dynamicArray(n,queries):
    result = []
    n = int(n)
    temp = []
    for _ in range(n):
        temp.append(list())
    lastAnswer = 0
    for i in range(len(queries)-1):
        first = queries[i][0]
        second = queries[i][1]
        val = queries[i][2]
        if first == 1:
            idx=((second ^ lastAnswer)%n)
            temp[idx].append(val)
        if first == 2:
            idx=((second ^ lastAnswer)%n)
            jidx = val%len(temp[idx])
            lastAnswer = temp[idx][jidx]
            result.append(lastAnswer)
    return result

if __name__ == "__main__":
    analyzer,source = util.start(dynamicArray)
    first_multiple_input = []
    data  = open("Questions/Question4/input/input10.txt",'r')
    first_multiple_input = list(map(int,data.readline().split()))
    n = int(first_multiple_input[0])
    q = int(first_multiple_input[1])
    queries = []
    for _ in range(q):
        queries.append(list(map(int, data.readline().split())))
    print("Test Case Prepared, Input taken")
    data.close()
    result = dynamicArray(n, queries)
    print(result)
    output = open("Questions/Question4/output/output10.txt")
    tcase = 1
    for _ in output:
        res = int(output.readline().split()[0])
        if res not in result:
            tcase=0
    if tcase == 1:
        print("Test Case Passed")
    else:
        print("Test Case Failed")
    util.report(analyzer,source,dynamicArray)

    
        
