import random

class Stack():

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

class setOfStacks(Stack):
    dishStack = []











N = 10

dish = Stack()
for _ in range(N):
    dish.push(random.randint(0,5))
