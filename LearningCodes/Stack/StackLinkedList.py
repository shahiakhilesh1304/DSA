from Node import Node


class StackLinkedList:
    """Stack implementation using Linked List"""

    def __init__(self):
        """Initialize an empty stack"""
        self.top = None
        self.size = 0

    def is_empty(self):
        """Check if stack is empty"""
        return self.top is None

    def push(self, data):
        """Push an element onto the stack"""
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
        print(f"Pushed {data} onto stack")

    def pop(self):
        """Remove and return the top element from the stack"""
        if self.is_empty():
            print("Stack Underflow! Stack is empty")
            return None

        popped_data = self.top.data
        self.top = self.top.next
        self.size -= 1
        print(f"Popped {popped_data} from stack")
        return popped_data

    def peek(self):
        """Return the top element without removing it"""
        if self.is_empty():
            print("Stack is empty")
            return None

        return self.top.data

    def get_size(self):
        """Return the size of the stack"""
        return self.size

    def display(self):
        """Display all elements in the stack"""
        if self.is_empty():
            print("Stack is empty")
            return

        print("Stack elements (top to bottom):")
        current = self.top
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example usage
if __name__ == "__main__":
    stack = StackLinkedList()

    print("=== Stack Operations ===")
    print(f"Is stack empty? {stack.is_empty()}")

    # Push operations
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)

    print(f"\nStack size: {stack.get_size()}")
    stack.display()

    # Peek operation
    print(f"\nTop element: {stack.peek()}")

    # Pop operations
    print("\n=== Pop Operations ===")
    stack.pop()
    stack.pop()

    print(f"\nStack size: {stack.get_size()}")
    stack.display()

    print(f"\nTop element: {stack.peek()}")

    # Pop remaining elements
    stack.pop()
    stack.pop()

    # Try to pop from empty stack
    print("\n=== Underflow Test ===")
    stack.pop()

    print(f"\nIs stack empty? {stack.is_empty()}")

