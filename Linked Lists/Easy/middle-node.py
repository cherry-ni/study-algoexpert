# O(n) time | O(1) space
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(linkedList):
    # Write your code here.
    length = 0
    node = linkedList
    while node is not None:
        node = node.next
        length += 1

    middle = length // 2

    for i in range(middle):
        linkedList = linkedList.next

    return linkedList