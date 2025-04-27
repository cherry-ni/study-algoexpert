# O(n) time | O(n) space
# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Write your code here.
    array = []
    recur(array, root, 0)
    return array


def recur(array, node, sum):
    if not node.left and not node.right:
        array.append(sum + node.value)
        return

    if node.left: recur(array, node.left, sum + node.value)
    if node.right: recur(array, node.right, sum + node.value)
