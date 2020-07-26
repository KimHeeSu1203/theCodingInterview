class Queue():
    queue = []
    def pop(self):
        if len(self.queue) > 0 :
            result = self.queue.pop(0)
        else:
            result = None
            print("Out of range")

        return result

    def push(self,item):
        self.queue.append(item)

    def peek(self):
        return self.queue[-1]

    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

    def min(self):
        temp = []
        min = 999
        for _ in range(len(self.queue)):
            min_a = self.queue.pop(0)
            temp.append(min_a) #새로 팝한 애가 min
            if min > min_a:
                min = min_a

        for _ in range(len(temp)):
            min_b = temp.pop(0)
            queue.push(min_b)

        return min


queue = Queue()
queue.push(2)
print(queue.min())
queue.push(3)
print(queue.min())
queue.push(1)
print(queue.min())
queue.push(4)
print(queue.min())

