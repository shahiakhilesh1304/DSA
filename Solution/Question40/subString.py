from Ruler import testCases
from Ruler import util


def hasSpecialSubstring(s: str, k: int) -> bool:
        if k > len(s):
            return False
        count = 0
        for i in range(len(s) - k + 1):
            substr = s[i:i + k]
            if len(set(substr)) == 1:
                if i > 0 and s[i - 1] != substr[0]:
                    if i + k < len(s) and s[i + k] != substr[0]:
                        count += 1
                    elif i + k >= len(s):
                        count += 1
                elif i == 0 and (i + k == len(s) or s[i + k] != substr[0]):
                    count += 1  
        return count > 0
    
if __name__ == "__main__":
    testcases = testCases.get_testcases(__file__)
    analyzer,source = util.start(hasSpecialSubstring)
    for input,output in testcases.items():
        file = open(input)
        string = file.readline().strip()
        k = int(file.readline().strip())
        res = hasSpecialSubstring(string,k)
        print(res)
        file.close()
        #Overriding the testcase validator
        out = open(output)
        expected = out.readline().strip()
        if str(res) == str(expected):
            print(f"Test Case Passed with Result {res} where expected is {expected}")
        else:
            print(f"Test Case Failed expected is {expected}")
        util.report(analyzer,source,hasSpecialSubstring)