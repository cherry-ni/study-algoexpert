# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        node = self
        while node is not None:
            if value < node.value:
                if node.left is None:
                    node.left = BST(value)
                    break
                else:
                    node = node.left

            else:
                if node.right is None:
                    node.right = BST(value)
                    break
                else:
                    node = node.right

        return self

    def contains(self, value):
        # Write your code here.
        node = self
        while node:
            if value < node.value:
                node = node.left
            elif value > node.value:
                node = node.right
            else:
                return True

        return False

    def find_successor(self):
        while self.left:
            self = self.left

        return self

    def remove(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        if not self:
            return self

        if value < self.value:
            if self.left:
                self.left = self.left.remove(value)
        elif value > self.value:
            if self.right:
                self.right = self.right.remove(value)
        else:
            if not self.right and not self.left:
                return None
            elif not self.right:
                self.value = self.left.value
                self.right = self.left.right
                self.left = self.left.left
                return self
            elif not self.left:
                self.value = self.right.value
                self.left = self.right.left
                self.right = self.right.right
                return self
            else:
                successor = self.right.find_successor()
                self.value = successor.value
                self.right = self.right.remove(successor.value)

        return self
