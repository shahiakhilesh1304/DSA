from Ruler import testCases
from Ruler import util
import math


def productGrid(grid):
    row = len(grid)
    col = len(grid[0])
    max__ = 0
    for i in range(row):
        for j in range(col):
            #UP
            if i-3 >= 0:
                prdt = grid[i][j]*grid[i-1][j]*grid[i-2][j]*grid[i-3][j]
                max__ = max(prdt,max__)
            #down
            if i+3 < row:
                prdt = grid[i][j]*grid[i+1][j]*grid[i+2][j]*grid[i+3][j]
                max__ = max(max__,prdt)
            #right
            if j+3 < col:
                prdt = grid[i][j]*grid[i][j+1]*grid[i][j+2]*grid[i][j+3]
                max__ = max(max__,prdt)
            #left
            if j-3 >= 0:
                prdt = grid[i][j]*grid[i][j-1]*grid[i][j-2]*grid[i][j-3]
                max__ = max(max__,prdt)
            
            #diagonal 
            #down right
            if i+3 < row and j+3 < col:
                prdt = grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3]
                max__ = max(prdt,max__)
            #down left diagonal
            if i+3 < row and j-3 >= 0:
                prdt = grid[i][j]*grid[i+1][j-1]*grid[i+2][j-2]*grid[i+3][j-3]
                max__ = max(prdt,max__)
            #Up Right
            if j-3 >= 0 and i-3 >= 0:
                prdt = grid[i][j]*grid[i-1][j-1]*grid[i-2][j-2]*grid[i-3][j-3]
                max__ = max(prdt,max__)     
            #Up left
            if j+3 < col and i-3 >= 0:
                prdt = grid[i][j]*grid[i-1][j+1]*grid[i-2][j+2]*grid[i-3][j+3]
                max__ = max(prdt,max__)
    return max__ 
        
    
if __name__ == "__main__":
    testcases = testCases.get_testcases(__file__)
    analyzer,source = util.start(productGrid)
    for input,output in testcases.items():
        file = open(input)
        grid = []
        for __ in range(0,20):
            n = list(map(int,file.readline().strip().split()))
            grid.append(n)
        result = productGrid(grid)
        print(result)
        file.close()
        result = testCases.validator([result],output)
        print(result,"\n\n")
        util.report(analyzer,source,productGrid)
        





