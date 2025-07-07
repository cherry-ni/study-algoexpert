# O(n) time | O(h) space
# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, isBalanced, height):
        self.isBalanced = isBalanced
        self.height = height


def heightBalancedBinaryTree(tree):
    # Write your code here.
    treeInfo = getTreeInfo(tree)
    return treeInfo.isBalanced


def getTreeInfo(node):
    if node == None:
        return TreeInfo(True, -1)

    leftSubTreeInfo = getTreeInfo(node.left)
    rightSubTreeInfo = getTreeInfo(node.right)

    isBalanced = leftSubTreeInfo.isBalanced and rightSubTreeInfo.isBalanced and abs(
        leftSubTreeInfo.height - rightSubTreeInfo.height) <= 1
    height = max(leftSubTreeInfo.height, rightSubTreeInfo.height) + 1
    return TreeInfo(isBalanced, height)
