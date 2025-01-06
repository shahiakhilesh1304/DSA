import math 
# from Ruler.Analyzer import BigOCalculator, analyze_complexity


# @analyze_complexity(inputs=[([1], 2), ([1, 2], 4), 
#                             ([1, 2, 3], 6), 
#                             ([1, 2, 3, 4], 5), 
#                             ([1, 2, 3, 4, 5], 15), 
#                             ([1, 2, 3, 4, 5, 6], 12), 
#                             ([10, 20, 30], 40), 
#                             ([5, 10, 15, 20], 25)])
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
    target = int(input("Enter the target: "))
    data = list(map(int,input("Enter the space separated array data: ").split()))
    result = sum_pair(data,target)
    print(f"Final OutPut: {result} ")