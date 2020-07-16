import unittest


def check(str1,str2):
    if len(str1)==len(str2):
        str1, str2 = sameLengthCheck(str1,str2)
    else:
        str1, str2 = diffLengthCheck(str1,str2)
    if(str1==str2):
        return True
    else:
        return False


def sameLengthCheck(str1,str2):
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            pop = i
    str1 = str1[:i-1]+str1[i+1:]
    str2 = str2[:i-1]+str2[i+1:]
    return str1, str2

def diffLengthCheck(str1, str2):
    flag = False
    longstr = str1 if len(str1)>=len(str2) else str2
    shortstr = str1 if len(str1)<len(str2) else str2

    for i in range(len(shortstr)):
        if shortstr[i] != longstr[i]:
            longstr = longstr[:i]+longstr[i+1:]
            flag = True
            break
    if flag == False:
        longstr = longstr[:-1]
    print(shortstr, longstr)
    return shortstr,longstr

class oneAway(unittest.TestCase):

    str_1 = ['pale','pales','pale','pale']
    str_2 = ['ple','pale','bale','bake']

    def testCase_1(self):
        for i in range(len(self.str_1)):
            result = check(self.str_1[i],self.str_2[i])
            self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
