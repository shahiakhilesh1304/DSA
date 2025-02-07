from Ruler import testCases
from Ruler import util
import math


def angryMasterJi(k,attendance):
    students = 0
    for i in attendance:
        if i<=0:
            students+=1
    if students >= k:
        return "NO"
    return "YES"

        
    
if __name__ == "__main__":
    testcases = testCases.get_testcases(__file__)
    analyzer,source = util.start(angryMasterJi)
    for input,output in testcases.items():
        file = open(input)
        t = int(file.readline().strip())
        res = []
        for _ in range(t):
            n,k = list(map(int,file.readline().strip().split()))
            attendance = list(map(int,file.readline().strip().split()))
            result = angryMasterJi(k,attendance)
            res.append(result)
        print(res)
        res = [1 if r == "YES" else 0 for r in res]
        file.close()
        result = testCases.validator(res,output)
        print(result,"\n\n")
        util.report(analyzer,source,angryMasterJi)
        





