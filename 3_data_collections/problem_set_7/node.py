class Node:
    """
    Node in a binary tree
    """

    def __init__(self, key=0):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    def get_key(self):
        return self.key

    def get_parent(self):
        return self.parent

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_key(self, key):
        self.key = key

    def set_parent(self, parent):
        self.parent = parent

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right
