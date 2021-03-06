from AVL.BSTNode import *

class BST:
    """ Naive implementation of a Height Augmented Binary Search Tree """
    def __init__(self):
        self.root = None
        self.stack = None


    def insert(self, key):
        # if root, just root = node with parent: None
        if self.root == None:
            self.root = BSTNode(key, None, None, None)

        #else find right place and right parent
        else:
            node = self.root
            ret = None
            for _ in range(height(self.root)+2):
                if key > node.key and node.right == None:
                    ret = node.right = BSTNode(key, None, None, node)
                    break
                elif key > node.key:
                    node = node.right
                    continue
                elif key < node.key and node.left == None:
                    ret = node.left = BSTNode(key, None, None, node)
                    break
                elif key < node.key:
                    node = node.left
                    continue

            update_heights(node.parent)
            return ret


    def find(self,key)->BSTNode:
        return find(self.root, key)


    def min(self):
        #go left till min
        node = min(self.root)
        return node.key


    def max(self):
        #go right till max
        node = self.root
        while(node.right is not None):
            node = node.right
        return node.key


    def delete(self, key)->bool:
        result = find(self.root, key)
        if result == None:
            return None
        else:
            node = delete(result)
            update_heights(node)
            return node

    def __iter__(self):
        self.stack = []
        node = self.root
        while node is not None:
            self.stack.append(node)
            node = node.left
        return self

    def __next__(self):
        if len(self.stack) == 0:
            raise StopIteration
        else:
            node = self.stack.pop()
            next = node.key
            if node.right is not None:
                node = node.right
                while node is not None:
                    self.stack.append(node)
                    node = node.left
            return next
