"""
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
"""

class threeInoneStack():
    def __init__(self,stackSize):
        self.stackLen = 3
        self.stackSize = stackSize
        self.arr = [None] * self.stackLen * self.stackSize
        self.size = [0] * self.stackLen

    def push(self,stackNum, item):
        if self.isFull(stackNum):
            raise Exception("Stack is Full")
        min,max = self.stackState(stackNum)
        now = min + self.size[stackNum-1]
        self.arr[now] = item
        self.size[stackNum-1] = self.size[stackNum-1]+1
        print(self.arr)

    def pop(self,stackNum):
        if self.size[stackNum-1]>0:
            min, max = self.stackState(stackNum)
            now = min + self.size[stackNum - 1] - 1
            self.arr[now] = None
            self.size[stackNum-1] = self.size[stackNum-1]-1
        else:
            raise Exception("Stack is Empty")
        print(self.arr)


    def isFull(self,stackNum):
        if self.size[stackNum-1] == self.stackSize:
            return True
        return False

    def stackState(self,stackNum):
        min,max = (stackNum-1)*(self.stackSize), stackNum*(self.stackSize)-1
        return min,max




myStack = threeInoneStack(2)
myStack.push(3, 1)
myStack.push(3, 2)
myStack.pop(3)
myStack.push(3, 3)
myStack.push(2, 1)
myStack.pop(2)



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