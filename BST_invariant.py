from is_sorted import is_sorted
from AVL.BST import BST

def is_in_order(tree: BST)->bool:
    l = []
    for k in tree:
        l.append(k)
    return is_sorted(l)
