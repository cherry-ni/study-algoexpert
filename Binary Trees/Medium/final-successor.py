# O(h) time | O(1) space
# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    # Write your code here.
    if node.right:
        return getMostLeftChild(node.right)

    else:
        return getMostRightParent(node)

def getMostLeftChild(node):
    while node.left:
        node = node.left

    return node

def getMostRightParent(node):
    while node.parent and node == node.parent.right:
        node = node.parent

    return node.parent