# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def findKthLargestValueInBst(tree, k):
    # Write your code here.
    output = []
    inOrderTraverse(tree, output)

    return output[-k]

#O(n) time | O(n) space
def inOrderTraverse(tree, array):
    if tree.left:
        inOrderTraverse(tree.left, array)
    array.append(tree.value)
    if tree.right:
        inOrderTraverse(tree.right, array)

class TreeInfo:
    def __init__(self, visited, lastValue):
        self.visited = visited
        self.lastValue = lastValue

# O(h + k) time | O(h) space
def findKthLargestValueInBst2(tree, k):
    # Write your code here.
    treeInfo = TreeInfo(0, -1)
    reverseInOrderTraverse(tree, k, treeInfo)

    return treeInfo.lastValue


def reverseInOrderTraverse(node, k, treeInfo):
    if node == None or treeInfo.visited >= k:
        return

    reverseInOrderTraverse(node.right, k, treeInfo)

    if treeInfo.visited < k:
        treeInfo.visited += 1
        treeInfo.lastValue = node.value
        reverseInOrderTraverse(node.left, k, treeInfo)

