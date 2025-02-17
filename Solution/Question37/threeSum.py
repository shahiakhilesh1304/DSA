from Ruler import testCases
from Ruler import util


def threeSum(nums: list[int]) -> list[list[int]]:
        nums.sort() 
        result = []

        for i in range(len(nums) - 2):     
            if i > 0 and nums[i] == nums[i - 1]:
                continue    
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1 
                elif total > 0:
                    right -= 1 
                else:   
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result
    
if __name__ == "__main__":
    testcases = testCases.get_testcases(__file__)
    analyzer,source = util.start(threeSum)
    for input,output in testcases.items():
        file = open(input)
        x = list(map(int,file.readline().strip().split()))
        res = threeSum(x)
        print(res)
        file.close()
        ## Validator Overriding
        out = open(output)
        val1 = list(map(int,out.readline().strip().split()))
        val2 = list(map(int,out.readline().strip().split()))
        result = [val1,val2]
        if result == res:
            print(f"Test Case Passed with Result {result} where expected is {res}")
        else:
            print(f"Test Case Failed expected is {res}")
        print(result)
        util.report(analyzer,source,threeSum)
        





