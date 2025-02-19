from Ruler import testCases
from Ruler import util
from math import ceil


def maxSubstringLength(s: str, k: int) -> bool:
        i = 0
        count = 0
        string = list(s)
        while True:
            if k > len(string) or len(string) == k:
                break
            counter = 0
            substring = string[i:k]
            rest_string = string[0:i]+string[k:]
            for char in substring:
                if char in rest_string:
                    counter += 1
                    break
            if counter==0:
                count +=1 
            i += 1
            k += 1
        return count>0
    
if __name__ == "__main__":
    testcases = testCases.get_testcases(__file__)
    analyzer,source = util.start(maxSubstringLength)
    for input,output in testcases.items():
        file = open(input)
        string = file.readline().strip()
        k = int(file.readline().strip())
        res = maxSubstringLength(string,k)
        print(res)
        file.close()
        #Overriding the testcase validator
        out = open(output)
        expected = out.readline().strip()
        if str(res) == str(expected):
            print(f"Test Case Passed with Result {res} where expected is {expected}")
        else:
            print(f"Test Case Failed expected is {expected}")
        util.report(analyzer,source,maxSubstringLength)