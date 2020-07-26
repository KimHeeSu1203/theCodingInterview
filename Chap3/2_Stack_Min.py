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
        temp = []
        min = 999
        for _ in range(len(self.stack)):
            min_a = self.stack.pop()
            temp.append(min_a) #새로 팝한 애가 min
            if min > min_a:
                min = min_a

        for _ in range(len(temp)):
            min_b = temp.pop()
            stack.push(min_b)

        return min


stack = Stack()
stack.push(2)
print(stack.min())
stack.push(3)
print(stack.min())
stack.push(1)
print(stack.min())
stack.push(4)
print(stack.min())

