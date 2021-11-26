from double_linked_list import DoubleLinkedList


class Queue:

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
