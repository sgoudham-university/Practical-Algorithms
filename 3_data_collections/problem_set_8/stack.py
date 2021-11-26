class Stack:
    def __init__(self, size=0):
        self.__size = size
        self.arr = [0] * size
        self.top = -1

    def push(self, val):
        if self.top >= self.__size:
            print("StackOverflow Error :P")
        else:
            self.top += 1
            self.arr[self.top] = val

    def pop(self):
        if self.stack_empty():
            print("The stack is empty so there is nothing to pop")
        else:
            self.top -= 1
            return self.arr[self.top + 1]

    def peek(self):
        if self.stack_empty():
            print("The stack is empty so there is nothing to peek")
        else:
            return self.arr[self.top]

    def stack_size(self):
        return self.top + 1

    def stack_empty(self):
        return self.top == -1


if __name__ == "__main__":
    sa = Stack(10)
    print(sa.stack_empty())
    print(sa.stack_size())
    sa.push("test")
    sa.push("this")
    print(sa.stack_empty())
    print(sa.stack_size())
    print(sa.pop())
    print(sa.pop())
    print(sa.stack_empty())
    print(sa.stack_size())
