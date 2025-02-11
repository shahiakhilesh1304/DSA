from Ruler import testCases
from Ruler import util


def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
        merged = sorted(nums1 + nums2)
        n = len(merged)
        if n%2 == 0:
            return ((merged[n//2 - 1]+merged[n//2])/2)
        else:
            return merged[n//2]
    
if __name__ == "__main__":
    testcases = testCases.get_testcases(__file__)
    analyzer,source = util.start(findMedianSortedArrays)
    for input,output in testcases.items():
        file = open(input)
        x = list(map(int,file.readline().strip().split()))
        y = list(map(int,file.readline().strip().split()))
        res = int(findMedianSortedArrays(x,y))
        print(res)
        file.close()
        result = testCases.validator([res],output)
        print(result)
        util.report(analyzer,source,findMedianSortedArrays)
        





