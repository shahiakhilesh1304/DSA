from LinkedList import LinkedList
from Ruler import testCases
from Ruler import util



def display(head):
    result = []
    cursor = head
    while cursor:
        result.append(cursor.data)
        cursor = cursor.next
    return result        


if __name__ == "__main__":
    testcases = testCases.get_testcases(__file__)
    analyzer,source = util.start(display)
    for input,output in testcases.items():
        file = open(input)
        length = int(file.readline().strip().split()[0])
        llist = LinkedList()
        for _ in range(length):
            data = int(file.readline().strip().split()[0])
            llist.append(data)
        result = display(llist.head.next)
        for i in result:
            print(i)
        file.close()
        result = testCases.validator(result,output)
        print(result)
        util.report(analyzer,source,display)
        del llist
                    
        
        