import unittest

class URLify(unittest.TestCase):

    datas = ['ab cde hi','13hi nice to meet you ', 'much%20ado%20about%20nothing']

    def testURLify_1(self):
        for data in self.datas:
            for i in range(len(data)-1, -1, -1):
                if i == ' ':
                    data.replace(i,'%20')

            print(data)





if __name__ == "__main__":
    unittest.main()
