from single_node import SingleNode


class SingleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def empty(self):
        """O(1)"""

        return self.head is None

    def search_key(self, key):
        """
        Best Case: O(1)
        Worst Case: O(n)
        """

        node = self.head
        while node is not None and node.key != key:
            node = node.get_next()
        return node

    def insert_head(self, key):
        """O(1)"""

        node = SingleNode(key)
        if self.head is None:
            self.tail = node
        node.set_next(self.head)
        self.head = node

    def insert_tail(self, key):
        """O(1)"""

        tail_node = SingleNode(key)
        if self.tail is None:
            self.insert_head(key)
        else:
            self.tail.set_next(tail_node)
        self.tail = tail_node

    def size(self):
        """
        Best Case: O(1)
        Worst Case: O(n)
        """

        size = 0
        node = self.head
        while node is not None:
            size += 1
            node = node.get_next()
        return size

    def print_all_keys(self):
        """
        Best Case: O(1)
        Worst Case: O(n)
        """

        node = self.head
        all_keys = "["
        while node is not None:
            all_keys += f"{node.get_key()}, " if node.get_next() is not None else f"{node.get_key()}"
            node = node.get_next()
        all_keys += "]"

        print(all_keys)
