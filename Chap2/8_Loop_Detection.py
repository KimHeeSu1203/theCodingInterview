# 만난 이후 교차 시작 지점을 아는 방법을 잘 모르겠음


from Chap2.LinkedList import LinkedList

def solution(ll_a):
    nowA = ll_a.head
    nowB = ll_a.head.next

    for i in range(len(ll_a)):
        for j in range(1,len(ll_a)):
            if nowA == nowB:
                return nowA



def solution(ll_a):
    slowRunner = ll_a
    fastRunner = ll_a

    while 1:
        slow = slowRunner.head.next
        fast = fastRunner.head.next.next

        if(slow == fast):
            break

