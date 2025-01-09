import math 
from Ruler import util


def sum_pair(data,target):
    n = len(data)-1
    arr = sorted(data)
    result = list()
    if n<=1:
        result
    min_diff = math.inf
    i = 0
    j = n 
    while i < j:
        sum = arr[i]+arr[j]
        diff = abs(target-sum)
        if diff < min_diff:
            result = [arr[i],arr[j]]
            min_diff = diff
        elif diff == 0:
            result = [arr[i],arr[j]]
            return result
        
        if sum > target:
            j-=1
        elif sum < target:
            i+=1
    return result
    
if __name__ == "__main__":
    analyzer,source = util.start(sum_pair)
    target = int(input("Enter the target: "))
    data = list(map(int,input("Enter the space separated array data: ").split()))
    result = sum_pair(data,target)
    print(f"Final OutPut: {result} ")
    util.report(analyzer,source,sum_pair)