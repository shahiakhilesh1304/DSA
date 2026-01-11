


def merge(left,right):
    merged = []
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            merged.append(left[i])
            i+=1
        else:
            merged.append(right[j])
            j+=1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged 



def mergeSort(arr):
    if len(arr)<= 1:
        return arr
    mid = len(arr)//2
    left_half = arr[:mid]
    print("Left half:", left_half)
    right_half = arr[mid:]
    print("Right half:", right_half)
    sortedleft = mergeSort(left_half)
    print(sortedleft)
    sortedright = mergeSort(right_half)
    print(sortedright)
    return merge(sortedleft, sortedright)


if __name__ == "__main__":
    import random
    size = 10**5  # Size of the unsorted array
    unsorted_array = [random.randint(1, 10**6) for _ in range(size)]
    sorted_arr = mergeSort(unsorted_array)
    print("Sorted array is:", ' '.join(map(str, sorted_arr)))