from Ruler import testCases
from Ruler import util


def maxArea(height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        def area(l,w):
            return l*w
        while left<right:
            length = right - left
            width = min(height[left],height[right])
            area_ = area(length,width)
            max_area = max(max_area,area_)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area 
    
if __name__ == "__main__":
    testcases = testCases.get_testcases(__file__)
    analyzer,source = util.start(maxArea)
    for input,output in testcases.items():
        file = open(input)
        x = list(map(int,file.readline().strip().split()))
        res = maxArea(x)
        print(res)
        file.close()
        result = testCases.validator([res],output)
        print(result)
        util.report(analyzer,source,maxArea)
        





