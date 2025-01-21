from LinkedList import LinkedList,Node
from Ruler import testCases
from Ruler import util



def atNodeFromTail(head,position):
    cur = head
    stack = []
    while cur != None:
        stack.append(cur.data)
        cur = cur.next
    return stack[-position-1]

    
if __name__ == "__main__":
    testcases = testCases.get_testcases(__file__)
    analyzer,source = util.start(atNodeFromTail)
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
            position = int(file.readline().strip().split()[0])
            out = atNodeFromTail(llist.head,position)
            result.append(out)
        for i in result:
            print(i)
        file.close()
        result = testCases.validator(result,output)
        print(result,"\n\n")
        util.report(analyzer,source,atNodeFromTail)
        del llist
