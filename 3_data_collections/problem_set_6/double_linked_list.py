from double_node import DoubleNode


class DoubleLinkedList:

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

    def delete_key(self, key):
        """
        Best Case: O(1)
        Worst Case: O(n)
        """

        node = self.search_key(key)
        prev_node = node.get_prev()
        next_node = node.get_next()
        if prev_node:
            prev_node.set_next(next_node)
        if next_node:
            next_node.set_prev(prev_node)
        if node == self.tail:
            self.tail = node.get_prev()

    def insert_head(self, key):
        """O(1)"""

        node = DoubleNode(key)
        if self.head is None:
            self.tail = node
        if self.head:
            self.head.set_prev(node)
        node.set_next(self.head)
        self.head = node

    def delete_head(self):
        """O(1)"""

        if self.head is not None:
            new_head_node = self.head.get_next()
            self.head = new_head_node

    def insert_tail(self, key):
        """O(1)"""

        tail_node = DoubleNode(key)
        if self.tail is None:
            self.insert_head(key)
        else:
            self.tail.set_next(tail_node)
            tail_node.set_prev(self.tail)
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
