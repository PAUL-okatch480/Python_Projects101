#circular linked list
class circularNode:
    def __init__(self,data):
        self.data= data
        self.next= None
class CircularLinkedList:
    def __init__(self):
        self.tail= None

    def  insert_into_empty(self, data):
        new_node= circularNode(data)
        self.tail= new_node
        new_node.next= new_node
    #insert at beginning of circular node
    def insert_at_beginning(self, data):
        new_node = circularNode(data)
        if self.tail is None:
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
    def insert_at_end(self,data):
        new_node = circularNode(data)
        if self.tail is None:
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node = self.tail.next
            self.tail.next = new_node
            self.tail = new_node
    def traverse(self):
            if self.tail is None:
                return
            current = self.tail.next
            while True:
                print(current.data, end=" ->")
                current = current.next
                if current == self.tail.next:
                    break
            print("(back to head)")
    def search(self, value):
            if self.tail is None:
                return False
            current = self.tail.next
            while True:
                if current.data == value:
                    return value
                current = current.next
                if current == self.tail.next:
                    break
            return False
    def delete (self, value):
            if self.tail is None:
                return
            current = self.tail.next
            previous = self.tail
            while True:
                if current.data == value:
                    #only one node
                    if current == self.tail and current.next == self.tail:
                        self.tail = None
                    else:
                        previous.next = current.next
                        if current == self.tail:
                            self.tail = previous
                    return
                previous = current
                current = current.next
                if current == self.tail.next:
                    break
#display results
    
inserr = CircularLinkedList()

inserr.insert_into_empty(10)
inserr.insert_at_end(20)
inserr.insert_at_end(30)
inserr.insert_at_beginning(5)

inserr.traverse()