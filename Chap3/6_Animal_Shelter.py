#먼저 온 애가 먼저 나가야 하니까 FIFO QUEUE
class Queue():
    order = 0
    dogqueue = []
    catqueue = []
    def dequeueAny(self):
        if (len(self.dogqueue) > 0) or (len(self.catqueue)>0):
            firstAnimal = self.dogqueue if self.dogPeek()[0] < self.catPeek()[0] else self.catqueue

        else:
            return False
        return firstAnimal.pop(0)
        """
        longQueue = self.dogqueue if len(self.dogqueue)>len(self.catqueue) else self.catqueue
        if len(longQueue) > 0:
            result = longQueue.pop(0)
        else:
            return False
        return result
        """

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
            self.dogqueue.append((self.order,item))
        elif animal == "cat":
            self.catqueue.append((self.order,item))
        self.order = self.order + 1

    def dogPeek(self):
        return self.dogqueue[0]

    def catPeek(self):
        return self.catqueue[0]

    def isDogEmpty(self):
        if len(self.dogqueue) == 0:
            return True
        else:
            return False

    def isCatEmpty(self):
        if len(self.catqueue) == 0:
            return True
        else:
            return False


animalShelter = Queue()
animalShelter.enqueue("dog",1)
animalShelter.enqueue("cat",7)
animalShelter.enqueue("cat",9)
animalShelter.enqueue("cat",8)
animalShelter.enqueue("dog",2)
animalShelter.enqueue("dog",3)
animalShelter.enqueue("dog",4)
animalShelter.enqueue("dog",5)
animalShelter.enqueue("cat",7)
animalShelter.enqueue("cat",8)
animalShelter.enqueue("cat",9)
animalShelter.enqueue("cat",10)

print(animalShelter.dequeueAny())
print(animalShelter.dequeueAny())
print(animalShelter.dequeueAny())
print(animalShelter.dequeueAny())
print(animalShelter.dequeueAny())

"""
print(animalShelter.dequeueCat())
print(animalShelter.dequeueDog())
print(animalShelter.dequeueAny())
print(animalShelter.dequeueAny())
"""