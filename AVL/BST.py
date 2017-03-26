from AVL.BSTNode import *

class BST:
    """ Naive implementation of a Height Augmented Binary Search Tree """
    def __init__(self):
        self.root = None


    def insert(self, key):
        # if root, just root = node with parent: None
        if self.root == None:
            self.root = BSTNode(key, None, None, None)

        #else find right place and right parent
        else:
            node = self.root
            for _ in range(height(self.root)+1):
                if key > node.key and node.right == None:
                    node.right = BSTNode(key, None, None, node)
                elif key > node.key:
                    node = node.right
                    continue
                elif key < node.key and node.left == None:
                    node.left = BSTNode(key, None, None, node)
                elif key < node.key:
                    node = node.left

            #update height all the way up
            while(node is not None):
                node.update_height()
                node = node.parent


    def find(self,key)->BSTNode:
        return find(self.root, key)


    def min(self):
        #go left till min
        node = self.root
        while(node.left is not None):
            node = node.left
        return node.key


    def max(self):
        #go right till max
        node = self.root
        while(node.right is not None):
            node = node.right
        return node.key

    #TODO: make sure this is broken, fix it.
    def delete(self, key)->bool:
        result = find(self.root, key)
        if result == None:
            return False
        else:
            #Found it.
            if result.right is not None:
                #TODO
            elif result.left is not None:
                #TODO
            else:
                result = None

            return True;
