# O(n + m) time | O(1) space
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergingLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
    firstLen = getLength(linkedListOne)  # O(n)
    secondLen = getLength(linkedListTwo)  # O(m)

    if firstLen > secondLen:
        while firstLen != secondLen:
            linkedListOne = linkedListOne.next
            firstLen -= 1
    else:
        while firstLen != secondLen:
            linkedListTwo = linkedListTwo.next
            secondLen -= 1

    while linkedListOne != linkedListTwo and (linkedListOne or linkedListTwo):
        linkedListOne = linkedListOne.next
        linkedListTwo = linkedListTwo.next

    return linkedListOne


def getLength(node):
    len = 0

    while node:
        len += 1
        node = node.next

    return len