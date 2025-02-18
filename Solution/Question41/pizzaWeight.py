from Ruler import testCases
from Ruler import util
from math import ceil


def maxWeight(pizzas: list[int]) -> int:
        pizzas.sort()
        length = len(pizzas)
        total_moves = ceil(length/4)
        odd_move = ceil(total_moves/2)
        even_move = total_moves - odd_move
        total_weight = 0
        l = length - 1 
        for _ in range(odd_move):
            total_weight += pizzas[l]  
            l -= 1  
        for _ in range(even_move):
            l -= 1 
            total_weight += pizzas[l] 
            l -= 1  
        return total_weight 
    
if __name__ == "__main__":
    testcases = testCases.get_testcases(__file__)
    analyzer,source = util.start(maxWeight)
    for input,output in testcases.items():
        file = open(input)
        pizzas = list(map(int,file.readline().strip().split()))
        res = maxWeight(pizzas)
        print(res)
        file.close()
        result = testCases.validator([res],output)
        print(result)
        util.report(analyzer,source,maxWeight)