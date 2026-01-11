from DSA import Node

class SinglyLinkedList:
    def __init__(self, mode="LIFO"):
        self.start = None
        self.mode = mode.upper()  # "LIFO" or "FIFO"

    def insert_at_start(self,data):
        newNode = Node(data)
        if self.start is None:
            self.start = newNode
        else:
            newNode.next = self.start
            self.start = newNode
            
    def display(self,Text=None):
        current = self.start
        if not current:
            print("Empty list")
            return
        if Text:
            print(Text, end=" ")
        while current:
            print(f"{current.data}", end=" -> ")
            current = current.next
    
    @property
    def is_empty(self):
        return self.start is None
    
    @property
    def iterate(self):
        current = self.start
        while current:
            yield current.data
            current = current.next
    @property
    def length(self):
        count = 0
        current = self.start
        while current:
            count += 1
            current = current.next
        return count
    
    def delete(self,key):
        current = self.start
        previous = None
        while current and current.data != key:
            previous = current
            current = current.next
        if current is None:
            return "Data not found to be deleted"
        else:
            if previous is None:
                self.start = current.next
            else:
                previous.next = current.next
        return f"Data {key} deleted successfully"
        
        
    def search(self, key):
        current = self.start
        while current:
            if current.data == key:
                return True
            current = current.next
        return False
    
    def delete_last(self):
        if self.start is None:
            return False
        if self.start.next is None:
            self.start = None
            return True
        current = self.start
        step_ahead = current.next.next
        while step_ahead:
            current = current.next
            step_ahead = step_ahead.next
        current.next = None
        return True
    
    @property
    def pop(self):
        """
        Remove and return element from the linked list.
        Uses self.mode to determine LIFO or FIFO behavior.
        Set mode using: linked_list.mode = "LIFO" or "FIFO"
        """
        if self.start is None:
            return None
        
        if self.mode == "LIFO":
            # Remove from start (Last In First Out)
            data = self.start.data
            self.start = self.start.next
            return data
        
        elif self.mode == "FIFO":
            # Remove from end (First In First Out)
            if self.start.next is None:
                data = self.start.data
                self.start = None
                return data
            
            current = self.start
            step_ahead = current.next.next
            while step_ahead:
                current = current.next
                step_ahead = step_ahead.next
            
            data = current.next.data
            current.next = None
            return data
        
        else:
            return None


    def append(self, data):
        newNode = Node(data)
        current = self.start
        if current is None:
            self.start = newNode
            return
        while current.next:
            current = current.next
        current.next = newNode
    
    def insert_at_POS(self,data,POS):
        newNode = Node(data)
        if self.start is None:
            self.start = newNode
            return
        if POS == 0:
            newNode.next = self.start
            self.start = newNode
            return
        current = self.start
        count = 0
        while current and count < POS -1:
            current = current.next
            count += 1
        if current is None:
            return "Position is not found"
        else:
            newNode.next = current.next
            current.next = newNode
    
    @property
    def reverse(self):
        previous = None
        current = self.start
        while current.next:
            nextNode = current.next
            current.next,previous = previous,current
            current = nextNode
        current.next = previous
        self.start = current

    def clear(self):
        self.start = None
    
    