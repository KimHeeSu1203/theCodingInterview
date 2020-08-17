
class Node:
    def __init__(self, item):
        self.right = None
        self.left = None
        self.val = item

    def __str__(self):
        return '('+str(self.left)+':L ' + "V:" + str(self.val) + " R:" + str(self.right)+')'

def initiateArrayToBinary(array):
    return arrayToBinary(array, 0, len(array) - 1)


def arrayToBinary(Arr,start,end):
    if start > end :
        return ''
    mid = (start+end)//2
    root = Node(Arr[mid])

    root.left = arrayToBinary(Arr,start,mid-1)
    root.right = arrayToBinary(Arr, mid+1, end)

    return root

testArr = [0,1,10,33,47,59,72,111,130]
print(initiateArrayToBinary(testArr))
