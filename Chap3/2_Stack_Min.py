class Stack():
    stack = []
    def pop(self):
        if len(self.stack) > 0 :
            result = self.stack.pop()

        else:
            result = None
            print("Out of range")

        return result

    def push(self,item):
        self.stack.append(item)

    def peek(self):
        return self.stack[-1]

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def min(self):
        temp_stack = Stack()
        min = stack.pop()
        temp_stack.push(min)

        while len(stack.stack) == 0:
            min_a = stack.pop()
            temp_stack.push(min_a)
            if min > min_a:
                min = min_a

        while len(temp_stack.stack) == 0:
            stack.push(temp_stack.pop())

        return min








stack = Stack()
stack.push(2)
print(stack.min())
stack.push(3)
print(stack.min())
stack.push(1)
print(stack.min())
stack.push(0)
print(stack.min())


