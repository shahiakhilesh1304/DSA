from Ruler import testCases
from Ruler import util



def triplet(arr1,arr2):
    if len(arr1) != len(arr2):
        return []
    reward = [0,0]
    for i in range(3):
        if int(arr1[i])<int(arr2[i]):
            reward[1] = reward[1]+1
        elif int(arr1[i])>int(arr2[i]):
            reward[0] = reward[0]+1
        elif int(arr1[i])==int(arr2[i]):
            pass
    return reward
    
    
if __name__ == "__main__":
    testcases = testCases.get_testcases(__file__)
    analyzer,source = util.start(triplet)
    for input,output in testcases.items():
        file = open(input)
        arr1 = file.readline().strip().split()
        arr2 = file.readline().strip().split()
        print(arr1)
        print(arr2)
        
        result = triplet(arr1,arr2)
        print(result)
        file.close()
        result = testCases.validator(result,output)
        print(result,"\n\n")
        util.report(analyzer,source,triplet)
