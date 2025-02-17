from Ruler import testCases
from Ruler import util


def minimumEffort(tasks: list[list[int]]) -> int:
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)
        min_energy = 0 
        curr_energy = 0
        for actual, minimum in tasks:
            if curr_energy < minimum:
                min_energy += (minimum - curr_energy)
                curr_energy = minimum
            curr_energy -= actual
        return min_energy
    
if __name__ == "__main__":
    testcases = testCases.get_testcases(__file__)
    analyzer,source = util.start(minimumEffort)
    for input,output in testcases.items():
        file = open(input)
        tasklist = list()
        while True:
            task = list(map(int,file.readline().strip().split()))
            if task:
                tasklist.append(task)
            else:
                break
        print(f"Task: {tasklist}")
        k = minimumEffort(tasklist)
        file.close()
        result = testCases.validator([k],output)
        print(result)
        util.report(analyzer,source,minimumEffort)