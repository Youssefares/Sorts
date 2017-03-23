def height(node:'BSTNode'):
    if node is None:
        return -1
    else:
        return node.height

class BSTNode:
    def __init__(self, key, left:'BSTNode', right:'BSTNode', parent:'BSTNode'):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent
        self.height = 0

    def update_height(self):
        self.height = max(height(self.left), height(self.right)) + 1
