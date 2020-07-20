#hash 테이블로 푸는게 제일 나을 수도 있다

#from LinkedList import LinkedList
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        HeadNode = Node("HEAD")
        self.head = HeadNode
        self.tail = HeadNode
        self.NumOfData = 0

    def insert(self,data):
        insertNode = Node(data)
        self.tail.next = insertNode
        self.tail = insertNode
        self.NumOfData += 1

    def delete(self):
        if self.NumOfData == 0:
            print("List is empty!")
            return False
        elif self.NumOfData == 1:
            delete_node = self.head.next
            self.head.next = None
            self.tail = self.head
            self.NumOfData -= 1
            print("리스트에서", delete_node.data, "데이터를 삭제하였습니다.")
            return delete_node.data
        else:
            delete_node = self.head.next
            self.head.next = self.head.next.next
            self.NumOfData -= 1
            print("리스트에서 ", delete_node.data, "데이터를 삭제하였습니다.")
            return delete_node.data

    def search(self, data):
        check = self.head
        for i in range(self.NumOfData):
            if check.next.data == data:
                print(data, "데이터는", i + 1, "번째에 있습니다.")
                return None
            check = check.next
        print(data, "데이터는 리스트에 없습니다.")
        return None

    def listNum(self):
        print("현재 리스트에는", self.NumOfData, "개의 요소가 있습니다.")
        return self.NumOfData

    def printList(self):
        current = self.head
        if self.NumOfData == 0:
            print("List is empty!")
            return None
        print("HEAD::", end='')
        for i in range(self.NumOfData - 1):
            print(current.next.data, "->", end='')
            current = current.next
        print(current.next.data)


ll = LinkedList()
ll.insert('a')
ll.insert('b')
ll.insert('c')
ll.insert('d')
ll.insert('e')
ll.insert('a')

datall = ll.head.next
hashll = {}

for i in range(ll.NumOfData):
    print(datall.data)
    if datall.data in hashll: #여기서 삭제해야 한다.
        del(hashll[datall.data])
        ll.delete()
    else:
        hashll[datall.data] = 1
    datall = datall.next

print(hashll)