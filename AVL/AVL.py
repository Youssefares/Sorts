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

        balance_diff = node.get_balance()
        if balance_diff > 1 and inserted_node.key < node.left.key:
            ##leftleft
            leftleft(node)
        elif balance_diff < 1 and inserted_node.key > node.right.key:
            ##rightright
            rightright(node)
        elif balance_diff > 1 and inserted_node.key > node.left.key:
            ##leftright
            leftright(node)
        elif balance_diff < 1 and inserted_node.key < node.right.key:
            ##rightleft
            rightleft(node)

        return inserted_node

    def delete(self, val):
        node = BST.delete(self, val)
        while node is not None:
            if abs(node.get_balance()) > 1:
                break
        if node is None:
            return

        if height(node.left) > height(node.right):
            if height(node.left.left) >= height(node.left.right):
                leftleft(node)
            else:
                leftright(node)
        elif height(node.right) > height(node.left):
            if height(node.right.right) >= height(node.right.left):
                rightright(node)
            else:
                rightleft(node)


    def print_height(self):
        print("Tree's height = ", height(self.root))


def leftleft(node):
    k1 = node.left
    k2 = node
    k2.left = k1.right
    k1.right = k2
    k1.parent = k2.parent
    k2.parent = k1
    update_heights(k2)

def rightright(node):
    k1 = node
    k2 = node.right
    k1.right = k2.left
    k2.left = k1
    k2.parent = k1.parent
    k1.parent = k2
    update_heights(k1)

def leftright(node):
    k1 = node.left
    k2 = node.left.right
    k3 = node
    k1.right = k2.left
    k3.left = k2.right
    k2.left = k1
    k2.right = k3
    k2.parent = k3.parent
    k1.parent = k3.parent = k2
    update_heights(k1)
    update_heights(k3)

def rightleft(node):
    k1 = node
    k2 = node.right.left
    k3 = node.right
    k1.right = k2.left
    k3.left = k2.right
    k2.left = k1
    k2.right = k3
    k2.parent = k1.parent
    k1.parent = k2.parent = k2
    update_heights(k1)
    update_heights(k3)
