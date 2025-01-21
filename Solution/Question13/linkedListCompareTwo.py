from LinkedList import LinkedList
from Ruler import testCases
from Ruler import util



def compareTwoLinkedLIst(head1,head2):
    same = 0
    cur1 = head1
    cur2 = head2
    while cur1.next is not None and cur2.next is not None:
        if cur1.data == cur2.data:
            same = 1
        else:
            return 0
        cur1 = cur1.next
        cur2 = cur2.next
    if cur1.next is None and cur2.next is None:
        return same
    else:
        return 0
    
    
if __name__ == "__main__":
    testcases = testCases.get_testcases(__file__)
    analyzer,source = util.start(compareTwoLinkedLIst)
    for input,output in testcases.items():
        file = open(input)
        nooftestcase = int(file.readline().strip().split()[0])
        result = []
        for _ in range(nooftestcase):
            length1 = int(file.readline().strip().split()[0])
            llist1 = LinkedList()
            for _ in range(length1):
                data = int(file.readline().strip().split()[0])
                llist1.append(data)
            length2 = int(file.readline().strip().split()[0])
            llist2 = LinkedList()
            for _ in range(length2):
                data = int(file.readline().strip().split()[0])
                llist2.append(data)
            out = compareTwoLinkedLIst(llist1.head,llist2.head)
            result.append(out)
        for i in result:
            print(i)
        file.close()
        result = testCases.validator(result,output)
        print(result,"\n\n")
        util.report(analyzer,source,compareTwoLinkedLIst)
        del llist1,llist2,result