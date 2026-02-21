
from DSA import Node

class Stack:
    def __init__(self):
        self.items = []
    
    @property
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty:
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty:
            return self.items[-1]
        else:
            raise IndexError("peek from empty stack")
        
    def size(self):
        return len(self.items)
    
    def display(self):
        return self.items
    
if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Stack items:", stack.display())
    print("Top item is:", stack.peek())
    print("Stack size is:", stack.size())
    print("Popped item is:", stack.pop())
    print("Stack items after pop:", stack.display())
    print("Is stack empty?", stack.is_empty)