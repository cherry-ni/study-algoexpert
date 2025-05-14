# O(n) time | O(d) space
def invertBinaryTree(tree):
    # Write your code here.
    if not tree:
        return

    if tree.left or tree.right:
        swapTree(tree)

    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)


def swapTree(node):
    temp = node.left
    node.left = node.right
    node.right = temp


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None