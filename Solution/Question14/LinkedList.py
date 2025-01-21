class Node:
    def __init__(self,data=None):
        """This helps to create a new node of the linked list

        Args:
            data (ANY): The data will be the value what you want to insert into the node . Node has two parts (Data and Next), here next referes to the address of the next node
        """
        self.data = data
        self.next = None
    
class LinkedList:
    """This will help you to implement the LinkedList
    """
    
    def __init__(self):
        """Creation of the head node which will never going to contain any actual data
        """
        
        self.head=Node()
         
    def append(self,data):
        """Append the new node to the current linked list

        Args:
            data (Any): THis will be append to the current linked list
        """
        new_node = Node(data)
        cursor = self.head
        while cursor.next!=None:
            cursor = cursor.next
        cursor.next = new_node    
        
        
    def display(self,head):
        result = []
        cursor = head
        while cursor:
            if cursor.data:
                result.append(cursor.data)
            cursor = cursor.next
        return result    

    def appendtohead(self,data,head):
        new_node = Node(data)
        if head==None:
            return new_node
        else:
            new_node.next = head
            head = new_node
        return new_node
    
    def insertNodeToAPosition(self,head,data,position):
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
        
    