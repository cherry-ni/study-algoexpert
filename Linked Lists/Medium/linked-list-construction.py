# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        # Write your code here.
        if self.head == node:
            return

        if self.tail == node or node.prev or node.next:
            self.remove(node)

        if self.head is None:
            self.head = node
            self.tail = node

        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
            node.prev = None

    def setTail(self, node):
        # Write your code here.
        if self.tail == node:
            return

        if self.head == node or node.prev or node.next:
            self.remove(node)

        if self.tail is None:
            self.head = node
            self.tail = node

        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            node.next = None

    def insertBefore(self, node, nodeToInsert):
        # Write your code here. nodeToInsert -> node
        if nodeToInsert.prev or nodeToInsert.next:
            self.remove(nodeToInsert)

        if node == self.head:
            self.setHead(nodeToInsert)
        else:
            prevNode = node.prev
            prevNode.next = nodeToInsert
            nodeToInsert.prev = prevNode
            nodeToInsert.next = node
            node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        # Write your code here node -> nodeToInsert
        if nodeToInsert.prev or nodeToInsert.next:
            self.remove(nodeToInsert)

        if node == self.tail:
            self.setTail(nodeToInsert)
        else:
            nextNode = node.next
            nextNode.prev = nodeToInsert
            nodeToInsert.prev = node
            nodeToInsert.next = nextNode
            node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        # Write your code here.
        node = self.head

        for _ in range(position - 1):
            node = node.next

        self.insertBefore(node, nodeToInsert)

    def removeNodesWithValue(self, value):
        # Write your code here.
        node = self.head
        while node is not None:
            if node.value == value:
                nextNode = node.next
                self.remove(node)
                node = nextNode
            else:
                node = node.next

    def remove(self, node):
        # Write your code here.
        if self.head == self.tail == node:
            self.head = None
            self.tail = None

        elif node == self.head:
            nextNode = node.next
            nextNode.prev = None
            self.head = nextNode
            node.next = None

        elif node == self.tail:
            prevNode = node.prev
            prevNode.next = None
            self.tail = prevNode
            node.prev = None

        else:
            prevNode = node.prev
            nextNode = node.next
            prevNode.next = nextNode
            nextNode.prev = prevNode
            node.prev = None
            node.next = None

    def containsNodeWithValue(self, value):
        # Write your code here.
        node = self.head
        while node is not None:
            if node.value == value:
                return True
            node = node.next
        return False