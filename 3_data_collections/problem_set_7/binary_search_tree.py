from node import Node

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def minimum(self):


    def maximum(self):

    def insert(self, key):
        insert_node = Node(key)
        current_node = self.root
        parent_node = None

        while not current_node:
            parent_node = current_node
            if key < current_node.get_key():
                current_node = current_node.get_left()
            else:
                current_node = current_node.get_right()

        insert_node.set_parent(parent_node)
        if not parent_node:
            self.root = insert_node
        elif insert_node.get_key() < parent_node.get_key():
            parent_node.set_left(insert_node)
        else:
            parent_node.set_right(insert_node)


    def search(self, node, key):
        if not node or key == node.get_left():
            return node
        if key < node.get_left():
            return self.search(node.get_left(), key)
        else:
            return self.search(node.get_right(), key)

    def size(self):

    def height(self):

    def traverse_in_order(self):

    def traverse_pre_order(self):

    def traverse_post_order(self):
