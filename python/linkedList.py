class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Linked list implementation with dummy nodes and length.
class LinkedList:
    def __init__(self):
        dummy_node = Node(-1)
        self.head = dummy_node
        self.tail = dummy_node
        self.length = 0

    def prepend(self, value):
        new_node = Node(value)
        if self.head == self.tail:
            self.tail = new_node
        new_node.next = self.head.next
        self.head.next = new_node
        self.length += 1

    def append(self, value):
        new_node = Node(value)
        if self.head == self.tail:
            self.head.next = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.length += 1
        
    def insert(self, value, index):
        if index == 0:
            self.prepend(value)
        elif index >= self.length:
            self.append(value)
        else:
            new_node = Node(value)
            prev = self.head
            curr = self.head.next
            i = 0
            while curr:
                if i == index:
                    new_node.next = curr
                    prev.next = new_node
                    self.length += 1
                    break
                i += 1
                prev = curr
                curr = curr.next

    def delete(self, value):
        if self.head == self.tail:
            raise ValueError("The list is empty.")
        else:
            prev = self.head
            curr = self.head.next
            while curr:
                if curr.value == value:
                    prev.next = curr.next
                    if curr == self.tail:
                        self.tail = prev
                    break
                prev = curr
                curr = curr.next

        raise ValueError("Value not found.")

    def search(self, value):
        if self.head == self.tail:
            return False
        else:
            curr = self.head.next
            while curr:
                if curr.value == value:
                    return True
                curr = curr.next
            return False
        
    def get(self, index):
        if self.head == self.tail:
            raise ValueError("The list is empty.")
        elif index >= self.length or index < 0:
            raise IndexError("Index out of bounds.")
        else:
            curr = self.head.next
            i = 0
            while curr:
                if i == index:
                    return curr.value
                i += 1
                curr = curr.next

    def size(self):
        return self.length
    
    def traverse(self):
        curr = self.head.next
        while curr:
            print(curr.value)
            curr = curr.next