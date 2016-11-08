"""Node implementation."""

# What to do when adding a value equal to the value of the node
class Node:

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def find(self, value):
        if self.value == valeu:
            return True
        elif self.value < value:
            return self.left.find(value)
        else:
            return self.right.find(value)

    def add(self, value):
        if self.value is None:
            self.value = value
        elif self.value < value:
            self.left.add(value)
        else:
            pass