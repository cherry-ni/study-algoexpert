# O(n) time | O(n) space
def inOrderTraverse(tree, array):
    # Write your code here.
    output = []
    inOrderTraverseRecur(tree, output)
    return output


def inOrderTraverseRecur(tree, output):
    if tree.left:
        inOrderTraverseRecur(tree.left, output)

    output.append(tree.value)

    if tree.right:
        inOrderTraverseRecur(tree.right, output)


def preOrderTraverse(tree, array):
    # Write your code here.
    output = []
    preOrderTraverseRecur(tree, output)
    return output


def preOrderTraverseRecur(tree, output):
    output.append(tree.value)

    if tree.left:
        preOrderTraverseRecur(tree.left, output)

    if tree.right:
        preOrderTraverseRecur(tree.right, output)


def postOrderTraverse(tree, array):
    # Write your code here.
    output = []
    postOrderTraverseRecur(tree, output)
    return output


def postOrderTraverseRecur(tree, output):
    if tree.left:
        postOrderTraverseRecur(tree.left, output)

    if tree.right:
        postOrderTraverseRecur(tree.right, output)

    output.append(tree.value)