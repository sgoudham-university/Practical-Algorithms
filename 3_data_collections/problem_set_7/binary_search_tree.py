from node import Node


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def minimum(self):
        node = self.root
        while node.get_left() is not None:
            node = node.get_left()
        return node

    def maximum(self):
        node = self.root
        while node.get_right() is not None:
            node = node.get_right()
        return node

    def insert(self, key):
        insert_node = Node(key)
        current_node = self.root
        parent_node = None

        while current_node is not None:
            parent_node = current_node
            if key < current_node.get_key():
                current_node = current_node.get_left()
            else:
                current_node = current_node.get_right()

        insert_node.set_parent(parent_node)

        if parent_node is None:
            self.root = insert_node
        elif insert_node.get_key() < parent_node.get_key():
            parent_node.set_left(insert_node)
        else:
            parent_node.set_right(insert_node)

    def search(self, node, key):
        if node is None or key == node.get_key():
            return node
        if key < node.get_key():
            return self.search(node.get_left(), key)
        else:
            return self.search(node.get_right(), key)

    def size(self, node):
        if node is None:
            return 0
        return 1 + self.size(node.left) + self.size(node.right)

    def height(self, node):
        if node is None or (node.get_left() is None and node.get_right() is None):
            return 0
        return 1 + max(self.height(node.get_left()), self.height(node.get_right()))

    def traverse_in_order(self, node):
        if node is not None:
            self.traverse_in_order(node.get_left())
            print(node.get_key(), end=" ")
            self.traverse_in_order(node.get_right())

    def traverse_pre_order(self, node):
        if node is not None:
            print(node.get_key(), end=" ")
            self.traverse_pre_order(node.get_left())
            self.traverse_pre_order(node.get_right())

    def traverse_post_order(self, node):
        if node is not None:
            self.traverse_post_order(node.get_left())
            self.traverse_post_order(node.get_right())
            print(node.get_key(), end=" ")

    def is_valid(self, node):
        return self.__is_valid(node)

    def __is_valid(self, node, maximum=None, minimum=None):
        if node is None:
            return True
        elif (maximum is not None and node.get_key() >= maximum) or (minimum is not None and node.get_key() <= minimum):
            return False
        else:
            return self.__is_valid(node.get_left(), node.get_key(), minimum) and self.__is_valid(node.get_right(), maximum, node.get_key())

    def get_root(self):
        return self.root


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(30)
    bst.insert(40)
    bst.insert(24)
    bst.insert(57)
    bst.insert(48)
    bst.insert(26)
    bst.insert(11)
    bst.insert(14)
    bst.insert(36)

    print(f"The Minimum Is: {bst.minimum().get_key()}")
    print(f"The Maximum Is: {bst.maximum().get_key()}")
    print(f"The Current Size (No. of Nodes) is: {bst.size(bst.get_root())}")
    print(f"The Current Height is: {bst.height(bst.get_root())}")
    print(f"Is This BST Valid?: {bst.is_valid(bst.get_root())}")
    print(f"Is Element 50 in BST: {bst.search(bst.get_root(), 50)}")
    print(f"Is Element 26 in BST: {bst.search(bst.get_root(), 26).get_key()}")

    print("\nPre-Order Traversal:")
    bst.traverse_pre_order(bst.get_root())

    print("\nIn-Order Traversal:")
    bst.traverse_in_order(bst.get_root())

    print("\nPost-Order Traversal:")
    bst.traverse_post_order(bst.get_root())
