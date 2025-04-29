# O(n) time | O(h) space
# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def evaluateExpressionTree(tree):
    # Write your code here.
    result = recur(tree)

    return result

def recur(node):
    if node.value > 0:
        return node.value

    if node.value == -1:
        return recur(node.left) + recur(node.right)
    elif node.value == -2:
        return recur(node.left) - recur(node.right)
    elif node.value == -3:
        return int(recur(node.left) / recur(node.right))
    elif node.value == -4:
        return recur(node.left) * recur(node.right)