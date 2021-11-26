class DoubleNode:

    def __init__(self, key, prev=None, next=None):
        self.key = key
        self.prev = prev
        self.next = next

    def set_key(self, key):
        self.key = key

    def set_prev(self, pointer):
        self.prev = pointer

    def set_next(self, pointer):
        self.next = pointer

    def get_key(self):
        return self.key

    def get_prev(self):
        return self.prev

    def get_next(self):
        return self.next