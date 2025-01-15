from LinkedList import LinkedList,Node
from Ruler import testCases
from Ruler import util



def insertNodeToAPosition(head,data,position):
    if head is None:
        return Node(data)
    current = head
    previous = head
    for _ in range(0,position+1):
        previous = current
        current = current.next
    new_node = Node(data)
    previous.next = new_node
    new_node.next = current
    return head        
    
    
if __name__ == "__main__":
    testcases = testCases.get_testcases(__file__)
    analyzer,source = util.start(insertNodeToAPosition)
    for input,output in testcases.items():
        file = open(input)
        length = int(file.readline().strip().split()[0])
        llist = LinkedList()
        for _ in range(length):
            data = int(file.readline().strip().split()[0])
            llist.append(data)
        data = int(file.readline().strip().split()[0])
        position = int(file.readline().strip().split()[0])
        res = insertNodeToAPosition(llist.head,data,position)
        result = llist.display(res)
        for i in result:
            print(i)
        file.close()
        result = testCases.validator(result,output)
        print(result,"\n\n")
        util.report(analyzer,source,insertNodeToAPosition)
        del llist 