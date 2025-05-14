# O(n) time | O(h) space
# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    # Write your code here.
    diameter, height = binaryTreeDiameterRecur(tree)

    return max(diameter, height)


def binaryTreeDiameterRecur(node):
    if node == None:
        return (0, 0)

    leftDiameter, leftHeight = binaryTreeDiameterRecur(node.left)
    rightDiameter, rightHeight = binaryTreeDiameterRecur(node.right)

    return (max(leftDiameter, rightDiameter, leftHeight + rightHeight), max(leftHeight, rightHeight) + 1)

