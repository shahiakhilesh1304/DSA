from LinkedList import LinkedList,Node
from Ruler import testCases
from Ruler import util



def deleteaNode(head,position):
    current = head
    prev = None
    
    if current == None:
        return head
    if position == 1:
        head = current.next 
    for _ in range(0, position+1):
        prev = current
        current = current.next
        if current is None:
            return head
        
    if current is not None:
        prev.next = current.next 
    return head
    
    
    
if __name__ == "__main__":
    testcases = testCases.get_testcases(__file__)
    analyzer,source = util.start(deleteaNode)
    for input,output in testcases.items():
        file = open(input)
        length = int(file.readline().strip().split()[0])
        llist = LinkedList()
        for _ in range(length):
            data = int(file.readline().strip().split()[0])
            llist.append(data)
        position = int(file.readline().strip().split()[0])
        res = deleteaNode(llist.head,position)
        result = llist.display(res)
        for i in result:
            print(i)
        file.close()
        result = testCases.validator(result,output)
        print(result,"\n\n")
        util.report(analyzer,source,deleteaNode)
        del llist 