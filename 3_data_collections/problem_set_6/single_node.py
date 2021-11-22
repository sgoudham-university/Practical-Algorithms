class SingleNode:

    def __init__(self, key, next=None):
        self.key = key
        self.next = next

    def set_key(self, key):
        self.key = key

    def set_next(self, pointer):
        self.next = pointer

    def get_key(self):
        return self.key

    def get_next(self):
        return self.next
