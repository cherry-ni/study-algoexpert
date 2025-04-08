# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(n) time | O(n) space
def reconstructBst(preOrderTraversalValues):
    # Write your code here.
    if not preOrderTraversalValues:
        return None

    node = BST(preOrderTraversalValues.pop(0))
    leftValues = [x for x in preOrderTraversalValues if x < node.value]
    rightValues = [x for x in preOrderTraversalValues if x >= node.value]

    node.left = reconstructBst(leftValues)
    node.right = reconstructBst(rightValues)

    return node
