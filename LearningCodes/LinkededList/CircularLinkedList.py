from Node import Node


class CircularLinkedList:
    def __init__(self):
        self.start = None
        
    def insert_at_start(self, data):
        newNode = Node()
        newNode.data = data
        if self.start is None:
            self.start = newNode
            newNode.next = newNode
            return
        else:
            current = self.start
            while current.next != self.start:
                current = current.next
            newNode.next = self.start
            current.next = newNode
            self.start = newNode
            return
        
    def append(self,data):
        newNode = Node()
        newNode.data = data
        if self.start is None:
            self.start = newNode
            newNode.next = newNode
        else:
            current = self.start
            startAddress = current
            while current and current.next != startAddress:
                current = current.next
            newNode.next = current.next
            current.next = newNode
            
    def delete(self,key):
        if self.start is None:
            return "List not found"
        current = self.start
        while current and current.next != self.start and current.data != key:
            previous = current
            current = current.next
        if current.data == key: 
            previous.next = current.next
                
    @property
    def iterate(self):
        current = self.start
        while current and current.next != self.start:
            yield (current.data,current.next)
            current = current.next
            
    @property
    def sort(self):
        current = self.start
        while current and current.next != self.start:
            index = current.next
            while index and index.next != self.start:
                if index.data > current.data:
                    index.data,current.data = current.data,index.data
                index = index.next
            current = current.next
            
    def display(self):
        if self.start is None:
            print("List is empty")
            return
        current = self.start
        startAddress = current
        while current and current.next != startAddress:
            print(current.data, end=" -> ")
            current = current.next
        print(current.data, "-> (back to start)")
        
    @property
    def length(self):
        count = 0
        current = self.start
        if self.start is None:
            return count
        startAddress = current
        while current and current.next != startAddress:
            count += 1
            current = current.next
        count += 1  
        return count
    @property
    def is_empty(self):
        return self.start is None

        
    @property
    def reverse(self):
        if self.start is None:
            return
        prev = None
        current = self.start
        startAddress = current
        nextNode = None
        while True:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
            if current == startAddress:
                break
        self.start.next = prev
        self.start = prev

    @property
    def clear(self): 
        self.start = None
        
    def insert_at_POS(self, data, pos): 
        newNode = Node()
        newNode.data = data
        current = self.start
        if self.start is None:
            self.start = newNode
            newNode.next = newNode
            return
        elif pos == 0:
            while current and current.next != self.start:
                current = current.next
            self.start = newNode
            current.next = newNode
            newNode.next = self.start
        elif pos > self.length:
            return "Wrong Invalid Position"
        else:
            previous = None
            current = self.start
            index = 0
            while index < pos:
                index += 1
                previous = current
                current = current.next
                if index == pos:
                    previous.next = newNode
                    newNode.next = current
    
    @property        
    def pop(self):
        if self.start is None:
            return "IndexOutOfBound"
        else:
            current = self.start
            previous = current
            while current and current.next != self.start:
                previous = current
                current = current.next
            data = current.data
            previous.next = self.start
            return data
            
            