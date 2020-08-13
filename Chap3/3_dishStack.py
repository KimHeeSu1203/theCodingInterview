import random

class setOfStack():
    def __init__(self):
        self.dishStack = []
        self.dishLimit = 3

    def pop(self):
        if len(self.dishStack) == 0:
                print("No dish")
                return 0

        if len(self.dishStack[-1]) > 0:
            self.dishStack[-1].pop()
            if len(self.dishStack[-1]) == 0:
                self.dishStack.pop()




    def push(self,data):
        # 이미 아무것도 없을때, 다 찼을 때
        if len(self.dishStack) == 0:
            dishStack = []
            self.dishStack.append(dishStack)

        elif len(self.dishStack[-1]) == self.dishLimit:
            dishStack = []
            self.dishStack.append(dishStack)

        self.dishStack[-1].append(data)


dish = setOfStack()
for _ in range(10):
    dish.push(random.randint(0,5))
    print(dish.dishStack)


for _ in range(11):
    dish.pop()
    print(dish.dishStack)