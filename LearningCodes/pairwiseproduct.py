def main(n,arr):
    result = []
    for i in range(n):
        for j in range(i + 1, n):
            result.append(arr[i] * arr[j])
    print(max(result))
    
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    main(n, arr)