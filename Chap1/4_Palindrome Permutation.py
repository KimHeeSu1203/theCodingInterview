import unittest

def makeDict(str_data): #아스키 코드 변환 시 대 -> 소 + 32 / 소 -> 대 - 32이라는 것을 명심
    dictData = {}
    A = ord('A')
    Z = ord('Z')

    for oneStr in str_data:
        if oneStr == ' ':
            continue
        if ord(oneStr)>=A and ord(oneStr)<=Z: #즉 대문자
            oneStr = chr(ord(oneStr)+32)
            print(oneStr)
        if oneStr in dictData.keys():
            dictData[oneStr] += 1
        else:
            dictData[oneStr] = 1
    return dictData


def testDict(dictData_Values):
    flag = False
    #홀수가 2번 나오는 순간 틀
    for i in dictData_Values:
        if i%2 == 1:
            if flag == True:
                return False
            else:
                flag = True
    return True



class palindrome(unittest.TestCase): #문제에서 대문자/소문자 구별 없이, 그리고 띄어쓰기는 무시하겠다 라는 것을 언급해야
    datas = ['tacTcoaa'] #대문자 확인하고싶어서 넣음

    def test_case1(self):
        for data in self.datas:
            dictData = makeDict(data)
            result = testDict(dictData.values())
            self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
