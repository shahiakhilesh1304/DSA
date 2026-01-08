def bSearch(arr,low,high,target):
    mid = (low+high)//2
    if low > high:
        return -1
    if arr[mid] == target:
        return mid+1
    elif arr[mid] < target:
        return bSearch(arr,mid + 1,high,target)
    else:
        return bSearch(arr,low,mid-1,target)
    
if __name__ == "__main__":
    arr = list(map(int,input("Enter the sorted array elements separated by space: ").split()))
    target = int(input("Enter the target element to search: "))
    result = bSearch(arr,0,len(arr)-1,target)
    if result != -1:
        print("Element is present at index", str(result))
    else:
        print("Element is not present in array")   


