from double_linked_list import DoubleLinkedList
from stack import Stack


class QueueBackedByDoublyLinkedList:

    def __init__(self):
        self.__doubly_linked_list = DoubleLinkedList()

    def enqueue(self, key):
        self.__doubly_linked_list.push(key)

    def dequeue(self):
        return self.__doubly_linked_list.pop()

    def peek(self):
        return self.__doubly_linked_list.peek()

    def size(self):
        return self.__doubly_linked_list.get_size()

    def is_empty(self):
        return self.__doubly_linked_list.is_empty()


class QueueBackedByTwoStacks:

    def __init__(self):
        self.__stack_one = Stack(100)
        self.__stack_two = Stack(100)

    def enqueue(self, key):
        """O(n)"""

        while not self.__stack_one.stack_empty():
            self.__stack_two.push(self.__stack_one.pop())
        self.__stack_one.push(key)
        while not self.__stack_two.stack_empty():
            self.__stack_one.push(self.__stack_two.pop())

    def dequeue(self):
        """O(1)"""

        return self.__stack_one.pop()