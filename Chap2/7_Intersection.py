#문제 이해를 못하겟다... 교차하는 연결리스트라는게 무슨 말이지?? -> 일단 풀긴 했음

from Chap2.LinkedList import LinkedList

def solution(ll_a, ll_b):
    longll,shortll = ll_a if len(ll_a)>=len(ll_b) else ll_b,ll_a if len(ll_a)<len(ll_b) else ll_b

    flag = True
    nowShort = shortll.head
    nowLong = longll.head

    for i in range(len(longll)-len(shortll)+1):
        nowLong = nowLong.next

    for i in range(len(nowShort)):
        if nowLong != nowShort:
            flag = False

    return flag

ll_a = LinkedList()
ll_a.generate(2, 0, 9)
ll_b = LinkedList()
ll_b.generate(3, 0, 9)
