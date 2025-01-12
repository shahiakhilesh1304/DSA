from LinkedList import LinkedList,Node
from Ruler import testCases
from Ruler import util



def display(head):
    result = []
    cursor = head
    while cursor:
        if cursor.data:
            result.append(cursor.data)
        cursor = cursor.next
    return result    

def appendtohead(data,head):
    new_node = Node(data)
    if head==None:
        return new_node
    else:
        new_node.next = head
        head = new_node
    return new_node
    
if __name__ == "__main__":
    testcases = testCases.get_testcases(__file__)
    analyzer,source = util.start(appendtohead)
    for input,output in testcases.items():
        file = open(input)
        length = int(file.readline().strip().split()[0])
        llist = LinkedList()
        for _ in range(length):
            data = int(file.readline().strip().split()[0])
            llist.head = appendtohead(data,llist.head)
        result = display(llist.head)
        for i in result:
            print(i)
        file.close()
        result = testCases.validator(result,output)
        print(result,"\n\n")
        util.report(analyzer,source,appendtohead)
        del llist 