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
    