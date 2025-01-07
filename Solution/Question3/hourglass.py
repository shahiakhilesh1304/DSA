def hourglassSum(arr):
    row_len = len(arr)
    col_len = len(arr[0])
    result = 0
    sum=0
    if row_len != 6 or col_len != 6:
        return result
    for i in range(0,row_len-2):
        for j in range(0,col_len-2):
            sum = (arr[i][j]+arr[i][j+1]+arr[i][j+2])+(arr[i+1][j+1])+(arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])
            if sum > result:
                result = sum
    return result

if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input(f"Enter {_+1}th row data space separated: ").split())))
        print("added ",_+1,"th row")
    result = hourglassSum(arr)
    print(result)
