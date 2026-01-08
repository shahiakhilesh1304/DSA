import random
def sSort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n) :
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

if __name__ == "__main__":
    size = 10**5  # Size of the unsorted array
    unsorted_array = [random.randint(1, 10**6) for _ in range(size)]
    # arr = list(map(int,input("Enter the array elements separated by space: ").split()))
    sorted_arr = sSort(unsorted_array)
    print("Sorted array is:", ' '.join(map(str, sorted_arr)))
    