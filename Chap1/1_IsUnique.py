#문자열 중복이 없는가?

import unittest

def unique(str_case):
    if len(str_case)>128:
        return False

    char_set = [False for _ in range(128)]

    for i in str_case:
        val = ord(i) # i의 아스키 번호 구하는게 ord
        if char_set[val]:
            return False
        char_set[val] = True

    return True

def findBack(str_case): #FB=Front&Back
    str_sort = sorted(str_case)

    for i in range(len(str_sort)-1):
        if str_sort[i] == str_sort[i+1]:
            return False

    return True

class IsUnique(unittest.TestCase):
    data = 'abcdefghijklmnop'

    def test_unique_1(self): #아스키 코드 길이 128이라고 미리 언급
        result = unique(self.data)
        self.assertTrue(result)


    def test_unique_2(self): #내가 생각한 방법, 추가공간 필요 없지만 문자열 바꿔도 된다고 안했음
        result = findBack(self.data)
        self.assertTrue(result)



if __name__ == "__main__":
    unittest.main()
