def findClosestValueInBst(tree, target):
    # Write your code here.
    node = tree
    result = node.value
    while node is not None:
        if abs(target - result) > abs(target - node.value):
            result = node.value

        if target > node.value:
            node = node.right

        elif target < node.value:
            node = node.left

        else:
            return node.value

    return result


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
