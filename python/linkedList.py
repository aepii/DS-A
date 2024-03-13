class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

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
        self.head.next = new_node

    def append(self, value):
        new_node = Node(value)
        if self.head == self.tail:
            self.head.next = new_node
        self.tail.next = new_node
        self.tail = new_node
        
    def insert(self, value, index):
        if index == 0:
            self.prepend(self, value)
        elif index >= 