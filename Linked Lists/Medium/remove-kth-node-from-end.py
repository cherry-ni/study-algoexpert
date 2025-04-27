# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    # Write your code here.
    node = head
    length = 1
    while node.next is not None:
        node = node.next
        length += 1

    node = head
    for _ in range(length - k):
        prevNode = node
        node = node.next

    if length - k == 0:
        nextNode = head.next
        head.value = head.next.value
        head.next = head.next.next
        nextNode.next = None

    else:
        prevNode.next = node.next