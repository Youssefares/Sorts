# TODO:
# [x] Search
# [ ] Insert
# [ ] Delete
# [x] Print Height

from AVL.BST import BST
from AVL.BSTNode import *

class AVL(BST):
    def __init__(self):
        BST.__init__(self)

    def search(self, val):
        return BST.find(self, val)

    def insert(self, val):
        BST.insert(self, val)
        # rebalance

    def delete(self, val):
        BST.delete(self, val)
        # rebalance

    def print_height(self):
        print("Tree's height = ", height(self.root))

    # def rebalance(self, node):
    # TODO
