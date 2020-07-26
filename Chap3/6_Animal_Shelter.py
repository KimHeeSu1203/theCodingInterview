#먼저 온 애가 먼저 나가야 하니까 FIFO QUEUE

class Queue():
    dogqueue = []
    catqueue = []
    def dequeueAny(self):
        longQueue = self.dogqueue if len(self.dogqueue)>len(self.catqueue) else self.catqueue
        if len(longQueue) > 0:
            result = longQueue.pop(0)
        else:
            return False
        return result

    def dequeueDog(self):
        if len(self.dogqueue) > 0:
            result = self.dogqueue.pop(0)
            return result

    def dequeueCat(self):
        if len(self.catqueue) > 0:
            result = self.catqueue.pop(0)
            return result

    def enqueue(self,animal,item):
        if animal == "dog":
            self.dogqueue.append(item)
        elif animal == "cat":
            self.catqueue.append(item)

    def peek(self):
        return self.queue[0]

    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False


animalShelter = Queue()
animalShelter.enqueue("dog",1)
animalShelter.enqueue("dog",2)
animalShelter.enqueue("dog",3)
animalShelter.enqueue("dog",4)
animalShelter.enqueue("dog",5)
animalShelter.enqueue("cat",7)
animalShelter.enqueue("cat",8)
animalShelter.enqueue("cat",9)
animalShelter.enqueue("cat",10)

print(animalShelter.dequeueAny())
print(animalShelter.dequeueCat())
print(animalShelter.dequeueDog())
print(animalShelter.dequeueAny())
print(animalShelter.dequeueAny())