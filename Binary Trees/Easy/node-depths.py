# O(n) time | O(h) space
def nodeDepths(root):
    # Write your code here.
    depthSum = getDepthSum(root, 0)

    return depthSum

def getDepthSum(node, depth):
    if not node:
        return 0

    return depth + getDepthSum(node.left, depth + 1) + getDepthSum(node.right, depth + 1)

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
