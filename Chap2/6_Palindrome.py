from Chap2.LinkedList import LinkedList

def solution(myLinked):
    list= []
    size = len(myLinked)

    nowLinked = myLinked.head

    if size%2 == 1:
        for i in range(int(size/2)):
            list.append(nowLinked.value)
            nowLinked = nowLinked.next
        nowLinked = nowLinked.next

    else:
        for i in range(size/2):
            list.append(nowLinked.value)
            nowLinked = nowLinked.next

    flag = True
    for i in range(1,int(size/2)+1):
        reverse = i * -1
        if(list[(-1)*i] != nowLinked.value):
            flag = False
        nowLinked = nowLinked.next
    return flag


ll_true = LinkedList([1, 2, 3, 4, 5, 4, 3, 2, 1])
print(solution(ll_true))
ll_false = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(solution(ll_false))