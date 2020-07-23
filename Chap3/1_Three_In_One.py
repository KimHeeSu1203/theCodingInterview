class Stack():
    stack = []
    def pop(self):
        if len(self.stack) > 0 :
            result = self.stack.pop()

        else:
            print("Out of range")

        return result

    def push(self,item):
        self.stack.push(item)

    def peek(self):
        return self.stack[-1]

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False


class threeInoneStack():
    def __init__(self,arr):
        len = int(len(arr)/3)
        oneStack =






myStack = Stack()
print(myStack.isEmpty())
arr = []
threeInoneStack(arr)


"""
class Queue():
    queue = []
    def remove(self):
        if len(self.queue) > 0 :
            result = self.queue.pop(0)

        else:
            print("Out of range")

        return result


    def add(self,item):
        self.queue.push(item)

    def peek(self):
        return self.queue[0]

    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False
"""