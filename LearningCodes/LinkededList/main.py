import SinglyLinkedList as ll
from DoublyLinkedList import DoublyLinkedList
from CircularLinkedList import CircularLinkedList
import random

def singly_linked_list_operations():
    linked_list = ll.SinglyLinkedList()
    n = int(input("Enter the number of elements to insert in the linked list: "))
    print(f"Generating {n} random numbers and inserting...")
    for _ in range(n):
        data = random.randint(1, 1000)
        linked_list.insert_at_start(data)
    
    print("The linked list is:")
    linked_list.display()
    
    print("The elements in the linked list are:")
    for data in linked_list.iterate:
        print(data, end=" ")
    print()
    
    print("The length of the linked list is:", linked_list.length)
    
    print("Deleting an element from the linked list.")
    key = int(input("Enter the value to delete from the linked list: "))
    linked_list.delete(key)
    print("The linked list after deletion is:")
    linked_list.display()
    print("The length of the linked list is:", linked_list.length)
    
    print("Deleting last element from the linked list.")
    linked_list.delete_last()
    print("The linked list after deletion is:")
    linked_list.display()
    print("The length of the linked list is:", linked_list.length)
    
    print("Checking if the linked list is empty:", linked_list.is_empty)
    print("Reversing the linked list.")
    linked_list.reverse
    print("The linked list after reversing is:")
    linked_list.display()
    
    print("Inserting elements in POSITION mode.")
    linked_list.insert_at_POS(32,2)
    linked_list.display()
    
    print("POP operation on the linked list.")
    linked_list.mode = "FIFO"
    data = linked_list.pop
    print(f"Popped element FIFO: {data}")
    linked_list.mode = "LIFO"
    data = linked_list.pop
    print(f"Popped element LIFO: {data}")
    print("The linked list after POP is:")
    linked_list.display()    
    
    print("Clearing the linked list.")
    linked_list.clear()
    print("The linked list after clearing is:")
    linked_list.display()
    print("The length of the linked list is:", linked_list.length)
    
def doubly_linked_list_operations():
    doubly_linked_list = DoublyLinkedList()
    n = int(input("Enter the number of elements to insert in the doubly linked list: "))
    print(f"Generating {n} random numbers and inserting...")
    for _ in range(n):
        data = random.randint(1, 1000)
        doubly_linked_list.append(data)
    
    print("The doubly linked list is:")
    doubly_linked_list.display
    
    print("The elements in the doubly linked list are:")
    none_id = id(None)
    for data, next_id, prev_id in doubly_linked_list.iterate:
        next_str = "None" if next_id == none_id else str(next_id)
        prev_str = "None" if prev_id == none_id else str(prev_id)
        print(f"[data:{data} | next Link:{next_str} | prev Link:{prev_str}]")
    
    print("The length of the doubly linked list is:", doubly_linked_list.length)
    
    pos = int(input("Enter the position to insert a new element in the doubly linked list: "))
    key = int(input("Enter the value to insert at position {}: ".format(pos)))
    doubly_linked_list.insert_at_pos(pos, key)
    print("The doubly linked list after insertion is:")
    doubly_linked_list.display
    
def circular_linked_list_operations():
    circular_linked_list = CircularLinkedList()
    n = int(input("Enter the number of elements to insert in the circular linked list: "))
    print(f"Generating {n} random numbers and inserting...")
    for _ in range(n):
        data = random.randint(1, 1000)
        circular_linked_list.append(data)
    
    
    print("Iterating through the circular linked list:")
    for data in circular_linked_list.iterate:
        print(data, end=" ")
    print()

    print("The circular linked list is:")
    circular_linked_list.display()
    
    print("The length of the circular linked list is:", circular_linked_list.length)
    
    print("Reversing the circular linked list.")
    circular_linked_list.reverse
    print("The circular linked list after reversing is:")
    circular_linked_list.display()
    
    pos = int(input("Enter the position to insert a new element in the circular linked list: "))
    key = int(input("Enter the value to insert at position {}: ".format(pos)))
    circular_linked_list.insert_at_POS(key, pos)
    print("The circular linked list after insertion is:")
    circular_linked_list.display()
    print("POP operation on the circular linked list.")
    data = circular_linked_list.pop
    print(f"Popped element: {data}")
    print("The circular linked list after POP is:")
    circular_linked_list.display()
    print("Clearing the circular linked list.")
    circular_linked_list.clear
    print("The circular linked list after clearing is:")
    circular_linked_list.display()

if __name__ == "__main__":
    #For Singly Linked List
    print("1. Singly Linked List Operations")
    print("2. Doubly Linked List Operations")
    print("3. Circular Linked List Operations")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            singly_linked_list_operations()
        case 2:
            doubly_linked_list_operations()
        case 3:
            circular_linked_list_operations()
        case _:
            print("Invalid choice. Please enter 1 or 2 or 3.")