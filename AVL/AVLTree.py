# TODO:
# [x] Search
# [x] Insert
# [x] Delete
# [x] Print Height

from AVL.BST import BST
from AVL.BSTNode import *

class AVL(BST):
    def __init__(self):
        BST.__init__(self)

    def search(self, val):
        return BST.find(self, val)

    def insert(self, val):
        inserted_node = BST.insert(self, val)
        node = inserted_node
        while node is not None:
            if abs(node.get_balance()) > 1:
                break
            node = node.parent

        if node is None:
            return inserted_node

        self.rebalance(node)

        return inserted_node

    def delete(self, val):
        node = BST.delete(self, val)
        while node is not None:
            if abs(node.get_balance()) > 1:
                break
            node = node.parent
        if node is None:
            return

        self.rebalance(node)


    def print_height(self):
        print("Tree's height = ", height(self.root))

    def right_rotate(self, node):
        k1 = node.left
        k2 = node
        k2.left = k1.right
        if k2.left is not None:
            k2.left.parent = k2
        k1.parent = k2.parent
        if node is self.root:
            self.root = k1
        else:
            if node.isLeftChild():
                node.parent.left = k1
            elif node.isRightChild():
                node.parent.right = k1
        k1.right = k2
        k2.parent = k1
        update_heights(k2)

    def left_rotate(self, node):
        k1 = node
        k2 = node.right
        k1.right = k2.left
        if k1.right is not None:
            k1.right.parent = k1
        k2.parent = k1.parent
        if node is self.root:
            self.root = k2
        else:
            if node.isLeftChild():
                node.parent.left = k2
            elif node.isRightChild():
                node.parent.right = k2
        k2.left = k1
        k1.parent = k2
        update_heights(k1)

    def rebalance(self, node):
        balance_diff = node.get_balance()
        if balance_diff > 1:
            if node.left.get_balance() >= 1:
                self.right_rotate(node)
            else:
                self.left_rotate(node.left)
                self.right_rotate(node)
        elif balance_diff < -1:
            if node.right.get_balance() <= -1:
                self.left_rotate(node)
            else:
                self.right_rotate(node.right)
                self.left_rotate(node)

