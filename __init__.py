"""DSA - Data Structure and Algorithm Practice"""

# Import Node class from nested location
try:
    # Try importing from nested LearningCodes structure
    from LearningCodes.LinkededList.Node import Node
except ImportError:
    # Fallback: define Node locally if nested import fails
    class Node:
        def __init__(self, data=None, next=None, prev=None):
            self.data = data
            self.next = next
            self.prev = prev

__all__ = ["Node"]

