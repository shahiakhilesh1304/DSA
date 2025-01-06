from Ruler.Analyzer import BigOCalculator, analyze_complexity

length = int(input("Enter the length of the array: "))
array_input = input(f"Enter the space Separated values for an array max number can be {length}: ")
data =  list(map(int,array_input.split()))[:length]

i = 0
@analyze_complexity(inputs=[[1],[1,2],[1,2,3],[1,2,3,4],[1,2,3,4,5],[1,2,3,4,5,6],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9,10]])
def main(data):
    result = []
    for j in range(len(data)-1,-1,-1):
        result.append(data[j])
    global i 
    i+=1
    return result
        

if __name__ == "__main__":
    result = main(data)
    print(f"Final output for the query is : {result}")
