#O(n) time | O(d) space
#This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def validateBst(tree):
    return validateBstRecur(tree, float('-inf'), float('inf'))

def validateBstRecur(tree, minValue, maxValue):
    if tree is None:
        return True
    if tree.value < minValue or tree.value >= maxValue:
        return False

    return validateBstRecur(tree.left, minValue, tree.value) and validateBstRecur(tree.right, tree.value, maxValue)