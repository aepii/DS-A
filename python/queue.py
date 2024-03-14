class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Stack is empty.")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Stack is empty.")
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

    