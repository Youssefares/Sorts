class BSTNode:
    def __init__(self, key, left:'BSTNode', right:'BSTNode', parent:'BSTNode'):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent
        self.height = 0

    def update_height(self):
        self.height = max(height(self.left), height(self.right)) + 1

    def get_balance(self):
        return height(self.left) - height(self.right)


# outside class to define the useful case that is height(nil/none/none) = -1
# makes code simpler and corner-case free everywhere else.
def height(node:'BSTNode'):
    if node is None:
        return -1
    else:
        return node.height

#helper functions
#TODO: do we move these inside the class?
def find(node:BSTNode, key)->BSTNode:
    if node == None or node.key == key:
        return node
    if key > node.key:
        return find(node.right, key)
    if key < node.key:
        return find(node.left, key)

def min(node: BSTNode)->BSTNode:
    while(node.left is not None):
        node = node.left
    return node

def delete(node: BSTNode):
    #When the parent dies, the grandpa has to be a parent to the children.
    grandpa = node.parent

    #if no children, just set corresponding child of parent to None
    if node.right is None and node.left is None:
        if node.key > grandpa.key:
            grandpa.right = None
        else:
            grandpa.left = None

    #if has one child: left, set parent to be grandpa, set corresponding child of grandpa to be child
    elif node.right is None:
        moving_node = node.left
        #parent-child handshake
        moving_node.parent = grandpa
        if node.key > grandpa.key:
            grandpa.right = moving_node
        else:
            grandpa.left = moving_node

    #if has one child: right, set parent to be grandpa, set corresponding child of grandpa to be child
    elif node.left is None:
        moving_node = node.right
        #parent-child handshake
        moving_node.parent = grandpa
        if node.key > grandpa.key:
            grandpa.right = moving_node
        else:
            grandpa.left = moving_node

    #if has both children
    else:
        #find min in right sub-tree, to keep in-order invariant
        moving_nowhere_node = min(node.right)
        #replace keys with node to be removed
        node.key = moving_nowhere_node.key
        #delete that min in right sub-tree
        delete(moving_nowhere_node)
