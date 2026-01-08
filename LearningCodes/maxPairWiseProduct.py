def max_pairwise_product(arr):
	n = len(arr)
	if n < 2:
		return 0
	max1 = max(arr[0], arr[1])
	max2 = min(arr[0], arr[1])
	for i in range(2, n):
		if arr[i] > max1:
			max2 = max1
			max1 = arr[i]
		elif arr[i] > max2:
			max2 = arr[i]
	return max1 * max2

if __name__ == "__main__":
	n = int(input())
	arr = list(map(int, input().split()))
	print(max_pairwise_product(arr))
