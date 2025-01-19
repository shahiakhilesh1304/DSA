from LinkedList import LinkedList,Node
from Ruler import testCases
from Ruler import util



def isCyclic(head):
    if head is None:
        return head
    visited = []
    while head.next != None:
        visited.append(head)
        head = head.next 
        while head in visited:
            return 1
    return 0 

    
if __name__ == "__main__":
    testcases = testCases.get_testcases(__file__)
    analyzer,source = util.start(isCyclic)
    for input,output in testcases.items():
        file = open(input)
        nooftestcase = int(file.readline().strip().split()[0])
        for _ in range(nooftestcase):
            index = int(file.readline().strip().split()[0])
            length = int(file.readline().strip().split()[0])
            llist = LinkedList()
            result = []
            for _ in range(length):
                data = int(file.readline().strip().split()[0])
                llist.append(data)
            extra = LinkedList(-1)
            temp = llist.head
            for i in range(length):
                if i == index:
                    extra = temp
                if i != length-1:
                    temp = temp.next
            temp.next = temp
            out = isCyclic(llist.head)
            result.append(out)
        for i in result:
            print(i)
        file.close()
        result = testCases.validator(result,output)
        print(result,"\n\n")
        util.report(analyzer,source,isCyclic)
        del llist
