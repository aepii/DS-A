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
        self.length += 1

    def append(self, value):
        new_node = Node(value)
        if self.head == self.tail:
            self.head.next = new_node
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1
        
    def insert(self, value, index):
        if index == 0:
            self.prepend(self, value)
        elif index >= self.length:
            self.append(self, value)
        else:
            new_node = Node(value)
            curr = self.head.next
            i = 0
            while curr:
                if i == index:
                    temp = curr
                    curr = new_node
                    curr.next = temp
                i += 1
                curr = curr.next
               