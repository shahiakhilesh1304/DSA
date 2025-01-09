from Ruler import util

def process(data):
    result = []
    for j in range(length-1,-1,-1):
        result.append(data[j])
    return result
        

if __name__ == "__main__":
    analyzer,source = util.start(process)
    length = int(input("Enter the length of the array: "))
    array_input = input(f"Enter the space Separated values for an array max number can be {length}: ")
    data =  list(map(int,array_input.split()))[:length]
    result = process(data)
    print(f"Final output for the query is : {result}")
    util.report(analyzer,source,process)
