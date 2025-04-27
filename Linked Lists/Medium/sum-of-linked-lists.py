# O(n) time | O(n) space
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
    firstNum = getNum(linkedListOne)
    secondNum = getNum(linkedListTwo)

    s = firstNum + secondNum

    node = LinkedList(s % 10)
    head = node
    if s < 10:
        return head

    s //= 10

    while s >= 10:
        node.next = LinkedList(s % 10)
        s //= 10
        node = node.next

    node.next = LinkedList(s)

    return head


def getNum(node):
    i = 1
    num = 0

    while node:
        num += i * node.value
        i *= 10
        node = node.next

    return num