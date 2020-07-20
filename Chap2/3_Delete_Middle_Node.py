from Chap2.LinkedList import LinkedList


def deleteMiddle(node): #두 문장의 순서도 중요하다, 값 먼저 바꾸고 next 변경
    node.value = node.next.value
    node.next = node.next.next

ll = LinkedList()
ll.add_multiple([1, 2, 3, 4])
middle_node = ll.add(5)
ll.add_multiple([7, 8, 9])

print(ll)
deleteMiddle(middle_node)
print(ll)

#헤드 접근 없이 삭제할 노드에만 접근이 가능하다는 것 / 나는 c에는 접근할 수 있다.
