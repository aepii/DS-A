class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        self.root = self._recursive_insert(self.root, value)

    def _recursive_insert(self, node, value):
        if node is None:
            node = BinaryNode(value)
            return node
        elif value > node.value:
            node.right = self._recursive_insert(node.right, value)
        elif value < node.value:
            node.left = self._recursive_insert(node.left, value)
        return node

    def search(self, value):
        pass