from double_node import DoubleNode


class DoubleLinkedList:

    def __init__(self):
        self.__head = None
        self.__tail = None

    def push(self, key):
        self.__insert_head(key)

    def pop(self):
        key = self.__head.get_key()
        self.__delete_head()
        return key

    def peek(self):
        return self.__head.get_key()

    def is_empty(self):
        return self.__empty()

    def get_size(self):
        return self.__size()

    def __empty(self):
        """O(1)"""

        return self.__head is None

    def __search_key(self, key):
        """
        Best Case: O(1)
        Worst Case: O(n)
        """

        node = self.__head
        while node is not None and node.key != key:
            node = node.get_next()
        return node

    def __delete_key(self, key):
        """
        Best Case: O(1)
        Worst Case: O(n)
        """

        node = self.__search_key(key)
        prev_node = node.get_prev()
        next_node = node.get_next()
        if prev_node:
            prev_node.set_next(next_node)
        if next_node:
            next_node.set_prev(prev_node)
        if node == self.__tail:
            self.__tail = node.get_prev()
        if node == self.__head:
            self.__head = node.get_next()

    def __insert_head(self, key):
        """O(1)"""

        node = DoubleNode(key)
        if self.__head is None:
            self.__tail = node
        if self.__head:
            self.__head.set_prev(node)
        node.set_next(self.__head)
        self.__head = node

    def __delete_head(self):
        """O(1)"""

        if self.__head is not None:
            if self.__tail == self.__head:
                self.__tail = self.__head.get_prev()
            node = self.__head
            self.__head = node.get_next()
            self.__head.set_prev(node.get_prev())

    def __insert_tail(self, key):
        """O(1)"""

        tail_node = DoubleNode(key)
        if self.__tail is None:
            self.__insert_head(key)
        else:
            self.__tail.set_next(tail_node)
            tail_node.set_prev(self.__tail)
        self.__tail = tail_node

    def __size(self):
        """
        Best Case: O(1)
        Worst Case: O(n)
        """

        size = 0
        node = self.__head
        while node is not None:
            size += 1
            node = node.get_next()
        return size

    def __print_all_keys(self):
        """
        Best Case: O(1)
        Worst Case: O(n)
        """

        node = self.__head
        all_keys = "["
        while node is not None:
            all_keys += f"{node.get_key()}, " if node.get_next() is not None else f"{node.get_key()}"
            node = node.get_next()
        all_keys += "]"

        print(all_keys)
