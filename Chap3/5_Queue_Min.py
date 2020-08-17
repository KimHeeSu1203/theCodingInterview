import random


class Stack():
    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            print("Out of range")

    def push(self, item):
        self.stack.append(item)

    def peek(self):
        return self.stack[-1]

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False


class MyQueue():
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def pop(self):
        for _ in range(len(self.stack1.stack)):
            self.stack2.push(self.stack1.pop())
        self.stack2.pop()
        print(self.stack1.stack)
        print(self.stack2.stack)
        print("-----------------")

    def push1(self, item):
        self.stack1.push(item)
        print(self.stack1.stack)
        print(self.stack2.stack)
        print(self.stack1)
        print(self.stack2)

        print("-----------------")


test = MyQueue()
for _ in range(10):
    test.push1(random.randint(0, 5))

"""
for _ in range(11):
    test.pop()
"""