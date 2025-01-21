from LinkedList import LinkedList,Node
from Ruler import testCases
from Ruler import util



def dropDuplicate(head):
    if head is None:
        return head
    head.next = dropDuplicate(head.next) # this will link every node to all the next coming nodes
    step_ahead = head.next
    if head.next is not None and step_ahead.data == head.data:
        return head.next
    return head
    
    
if __name__ == "__main__":
    testcases = testCases.get_testcases(__file__)
    analyzer,source = util.start(dropDuplicate)
    for input,output in testcases.items():
        file = open(input)
        nooftestcase = int(file.readline().strip().split()[0])
        result = []
        for _ in range(nooftestcase):
            length = int(file.readline().strip().split()[0])
            llist = LinkedList()
            for _ in range(length):
                data = int(file.readline().strip().split()[0])
                llist.append(data)
            res = dropDuplicate(llist.head)
            result = llist.display(res)
            for i in result:
                print(i)
            file.close()
            result = testCases.validator(result,output)
            print(result,"\n\n")
        util.report(analyzer,source,dropDuplicate)
        del llist
