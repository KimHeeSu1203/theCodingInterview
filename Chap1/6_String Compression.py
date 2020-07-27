import unittest


def makeCompression(str_data): #아스키 코드 변환 시 대 -> 소 + 32 / 소 -> 대 - 32이라는 것을 명심
    comp = []
    for oneStr in str_data:
        if len(comp)==0:
            comp.append(oneStr)
            comp.append(1)
        else:
            if(comp[-2:-1][0] == oneStr):
                num = comp.pop()
                comp.append(num+1)
            else:
                comp.append(oneStr)
                comp.append(1)

    strComp = ''.join(comp)
    print(strComp)
    return comp


def lengthCheck(list,data):
    if len(list)>=len(data):
        return False
    return True

class stringCompression(unittest.TestCase): #문제에서 대문자/소문자 구별 없이, 그리고 띄어쓰기는 무시하겠다 라는 것을 언급해야
    data = 'aabcccccaaa' #대문자 확인하고싶어서 넣음

    def test_case1(self):
        compData = makeCompression(self.data)
        result = lengthCheck(compData,self.data)
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
