def miniMaxSum(arr):
    # import pdb; pdb.set_trace()
    minSum = sum(arr)
    maxSum = 0
    if len(arr) < 4:
        print("0 0")
    for i in range(len(arr)):
        sum_ = 0
        for j in range(len(arr)):
            if j != i:
                sum_ += arr[j]
        minSum = min(sum_,minSum)
        maxSum = max(sum_,maxSum)
    print(f"{minSum} {maxSum}")
            
if __name__ == "__main__":
    arr = list(map(int, input().split()))
    miniMaxSum(arr)