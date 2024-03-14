class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        self._recursive_insert(self.root, value)

    def _recursive_insert(self, node, value):
        if node is None:
            node = BinaryNode(value)
            return
        elif value > node.value:
            self._recursive_insert(node.right, value)
        elif value < node.value:
            self._recursive_insert(node.left, value)

    def search(self, value):
        pass