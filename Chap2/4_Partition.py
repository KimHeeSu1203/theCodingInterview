from Chap2.LinkedList import LinkedList


def partition(ll,key):
    befLL = LinkedList()
    aftLL = LinkedList()
    keyLL = LinkedList()

    now = ll.head
    for _ in range(len(ll)):

        if now.value > key:
            aftLL.add(now.value)
        elif now.value == key:
            keyLL.add(now.value)
        elif now.value < key:
            befLL.add(now.value)
        now = now.next

    befLL.add_multiple(keyLL)
    befLL.add_multiple(aftLL)
    print(befLL)

ll = LinkedList()
ll.add_multiple([3,5,8,5,10,2,1])
key = 5
partition(ll,key)
