from LinkedList import LinkedList
from Ruler import testCases
from Ruler import util



def mergeTwoLinkedLIst(head1,head2):
    if head1 is None:
        return head2
    elif head2 is None:
        return head1
    if head1.data <= head2.data:
        head1.next = mergeTwoLinkedLIst(head1.next,head2)
        return head1
    else:
        head2.next = mergeTwoLinkedLIst(head1,head2.next)
        return head2
    
    
if __name__ == "__main__":
    testcases = testCases.get_testcases(__file__)
    analyzer,source = util.start(mergeTwoLinkedLIst)
    for input,output in testcases.items():
        file = open(input)
        nooftestcase = int(file.readline().strip().split()[0])
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
            out = mergeTwoLinkedLIst(llist1.head.next,llist2.head.next)
            result = llist1.display(out)
            for i in result:
                print(i)
            file.close()
            result = testCases.validator(result,output)
            print(result,"\n\n")
        util.report(analyzer,source,mergeTwoLinkedLIst)
        del llist1,llist2
