# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    node = linkedList

    if node is None:
        return None

    while node.next is not None and node.value == node.next.value:
        node.next = node.next.next

    node.next = removeDuplicatesFromLinkedList(node.next)

    return node