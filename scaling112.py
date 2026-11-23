#Implementing Doubly linked lists
#There must be a first 
class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    #inserting at the beginning
    def insert_at_beginning(self, data):
        new_node = DoublyNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
    #inserting at the end
    def insert_at_end(self, data):
        new_node = DoublyNode(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    #traversing forward
    def traverse_forward(self):
        current = self.head
        while current is not None:
            print(current.data, end=" <-> ")
            current = current.next
        print("None.")
    #traverse backward
    def traverse_backward(self):
        current = self.tail
        while current is not None:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None.")
    #searching doubly list
    def search (self, value):
        current= self.head
        while current is not None:
            if current.data == value:
                return True
            current = current.next
        return False
    #delete a node in doubly list
    def delete (self, value):
        current = self.head
        while current is not None:
            if current.data == value:
                if current.prev is not None:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next is not  None:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return
            current = current.next
dll = DoublyLinkedList() 
dll.insert_at_end(10) 
dll.insert_at_end(20) 
dll.insert_at_end(30) 
dll.traverse_forward() 
dll.traverse_backward() 
dll.delete(20) 
dll.traverse_forward() 