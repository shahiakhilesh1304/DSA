from Ruler import testCases
from Ruler import util


def removeElement(nums: list[int], val: int) -> int:
        k = 0
        for i,num in enumerate(nums):
            if num != val:
                nums[k] = nums[i]
                k += 1
        return k
    
if __name__ == "__main__":
    testcases = testCases.get_testcases(__file__)
    analyzer,source = util.start(removeElement)
    for input,output in testcases.items():
        file = open(input)
        nums = list(map(int,file.readline().strip().split()))
        print(f"Array: {nums}")
        val = int(file.readline().strip())
        print(f"Value to remove: {val}")
        k = removeElement(nums,val)
        print(f"Result: {nums[:k]}")
        nums[:k] = sorted(nums[:k])
        file.close()
        result = testCases.validator(nums[:k],output)
        print(result)
        util.report(analyzer,source,removeElement)
        





