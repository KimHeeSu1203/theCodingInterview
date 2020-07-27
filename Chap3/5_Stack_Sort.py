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

#추가적으로 하나의 스택은 쓸 수 있다는게 한칸을 더 만들 수 있다는건지 스택을 하나 더 만들 수 있다는건지 잘 모르곘음

def Sort(stack):
    tmp_stack = Stack()
    tmp = stack.pop()
    tmp_stack.push(tmp)
    for i in range(len(stack.stack)):
        if



myStack = Stack()
for i in range(5):
    myStack.push(i)
print(myStack)
Sort(myStack)
print(myStack)
