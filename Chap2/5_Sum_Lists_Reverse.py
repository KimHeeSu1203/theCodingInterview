from Chap2.LinkedList import LinkedList


def check10(longllData):
    if longllData.value > 10:
        longllData.next.value = longllData.next.value + 1
        longllData.value = longllData.value - 10


def solution(ll1,ll2):

    longll,shortll = ll1 if len(ll1)>=len(ll2) else ll2, ll1 if len(ll1)<len(ll2) else ll2
    nowLong = longll.tail
    nowShort = shortll.tail

    for i in range(len(shortll)):
        nowLong.value = nowLong.value + nowShort.value
        check10(nowLong)
        nowLong = nowLong.next
        nowShort = nowShort.next

    check10(nowLong)


ll_a = LinkedList()
ll_a.generate(2, 0, 9)
ll_b = LinkedList()
ll_b.generate(3, 0, 9)


solution(ll_a,ll_b)

print(ll_b)
