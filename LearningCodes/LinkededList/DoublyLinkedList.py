from DSA import Node

class DoublyLinkedList:
    def __init__(self):
        self.start = None


    def insert_at_start(self, data):
        newNode = Node()
        if self.start is None:
            newNode.data = data
            self.start = newNode
            return
        else:
            newNode.data = data
            newNode.next = self.start
            self.start.prev = newNode
            self.start = newNode
            return  
    
    def append(self,data):
        newNode = Node()
        if self.start is None:
            self.start = newNode
            newNode.data = data
            return 
        current = self.start
        while current.next:
            current = current.next
        newNode.data = data
        current.next = newNode
        newNode.prev = current    

    @property
    def display(self):
        current = self.start
        while current:
            next_link = id(current.next) if current.next else None
            prev_link = id(current.prev) if current.prev else None
            print(f"[data:{current.data} | next Link:{next_link} | prev Link:{prev_link}]", end="\n") 
            current = current.next 
    
    @property
    def length(self):
        count = 0
        current = self.start
        while current:
            count += 1
            current = current.next
        return count
    
    @property
    def is_Empty(self):
        return self.start is None

    @property    
    def iterate(self):
        current = self.start
        while current:
            yield (current.data, id(current.next), id(current.prev))
            current = current.next
    
    def insert_at_pos(self,pos,key):
        if pos < 0 or pos > self.length:
            print("Invalid Position")
            return
        newNode = Node()
        newNode.data = key
        if pos == 0:
            if self.start is None:
                self.start = newNode
                return
            else:
                newNode.next = self.start
                self.start.prev = newNode
                self.start = newNode
                return
        current = self.start
        previous = None
        count = 0
        while count < pos:
            previous = current
            current = current.next
            count += 1
            if count == pos:
                previous.next = newNode
                newNode.prev = previous
                newNode.next = current
                if current:
                    current.prev = newNode
                return

            
    def search(self,key):
        current = self.start
        while current:
            if current.data == key:
                return True
            current = current.next
        return False
    
    @property
    def sortSS(self):
        if self.start is None:
            return
        current = self.start
        while current:
            idec = current.next
            while idec:
                if current.data > idec.data:
                    current.data,idec.data = idec.data,current.data
                    idec = idec.next
                else:
                    idec = idec.next
            current = current.next
            
    
    def delete(self,key):
        current = self.start
        if self.start is None:
            return "List is not assigned"
        while current and current.data != key:
            current = current.next
        if current is None:
            return "Data not found"
        else:
            if current.prev is None:
                self.start = current.next
                if self.start:
                    self.start.prev = None
            else:
                current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
    
    @property        
    def clear(self):
        self.start = None    
            