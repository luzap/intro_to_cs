"""Custom binary tree node implementation."""


class Node:

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def find(self, value):
        """Recursive search for nodes containing a given value."""
        if self.value == value:
            return True
        else:
            if self.value > value:
                if not isinstance(self.left, Node):
                    return False
                else:
                    return self.left.find(value)
            elif self.value < value:
                if not isinstance(self.right, Node):
                    return False
                else:
                    return self.right.find(value)

    def add(self, value):
        """Adding to binary tree based on comparison first Node. There are only
        three possibilities for the values of any individual node. Either they
        are greater than, less than or equal to the value given.

        :param value: object
        :returns: None
        """

        if self.value is None:  # If not initialized, initializes
            self.value = value
        else:
            if self.value > value:
                # Checks whether or not the left node is a 
                # Node object
                if not isinstance(self.left, Node):
                    self.left = Node(value=value)
                else:
                    self.left.add(value)
            elif self.value < value:
                if not isinstance(self.right, Node):
                    self.right = Node(value=value)
                else:
                    self.left.add(value)

if __name__ == "__main__":
    node = Node()
    node.add(6)
    node.add(2)
    node.add(5)
    node.add(7)
    print(node.find(6))
    print(node.find(2))
    print(node.find(5))
    print(node.find(7))
    print(node.find(4))
    print(node.find(3))
    print(node.find(10))
