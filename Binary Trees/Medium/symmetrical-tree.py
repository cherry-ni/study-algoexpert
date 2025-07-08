# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def symmetricalTree(tree):
    # Write your code here.
    leftSubTree = [tree.left]
    rightSubTree = [tree.right]

    while len(leftSubTree) > 0:
        leftNode = leftSubTree.pop()
        rightNode = rightSubTree.pop()

        if leftNode and not rightNode:
            return False

        if not leftNode and rightNode:
            return False

        if not leftNode:
            continue

        if leftNode.value != rightNode.value:
            return False

        leftSubTree.append(leftNode.left)
        leftSubTree.append(leftNode.right)
        rightSubTree.append(rightNode.right)
        rightSubTree.append(rightNode.left)

    return True
