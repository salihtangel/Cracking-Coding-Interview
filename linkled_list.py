class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()
    def get_head(self):
        return self.head
    
    def deleteNode(self, data):
        new_node = self.head

        if new_node.data == data:
            return self.head.next
    
        while new_node.next != None:
            if new_node.data == data:
                new_node.next = new_node.next.next
                return self.head
        
            new_node = new_node.next
        return self.head