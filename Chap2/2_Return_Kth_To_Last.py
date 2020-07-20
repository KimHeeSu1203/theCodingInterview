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


def test1(ll, k):
    p1 = ll.head
    p2 = ll.head
    for i in range(ll.NumOfData):
        p1 = p1.next
        if ll.NumOfData <= k:
            print("문자열 길이 부족")
            break
        if (i >= k) & (p1 != ll.tail):
            p2 = p2.next
            print(p2.data, p1.data)

        elif (i >= k) & (p1 == ll.tail):
            p2 = p2.next
            print(p2.data)
    print("test1")

def test2(ll, k):
    p1 = ll.head
    p2 = ll.head
    for i in range(k):
        p1 = p1.next
        if p1 == ll.tail:
            print("문자열 길이 부족")

    for i in range(k, ll.NumOfData):
        p1 = p1.next
        p2 = p2.next
        print(p2.data, p1.data)
        if p1 == ll.tail:
            print(p2.data)
    print("test2")


#p1이 k개 이상 가면, p2가 오고, p1이 tail이면 p2가 답
ll = LinkedList()
ll.insert('a')
ll.insert('b')
ll.insert('c')
ll.insert('d')
ll.insert('e')
ll.insert('f')
ll.insert('g')



k = 3
p1 = ll.head
p2 = ll.head

test1(ll,k)
test2(ll,k)
