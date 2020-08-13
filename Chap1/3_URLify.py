import unittest

class URLify(unittest.TestCase):

    datas = ['ab cde hi','13hi nice to meet you ', 'much%20ado%20about%20nothing']
    new_data = [[] for _ in range(len(datas))]

    def testURLify_1(self):
        for data in self.datas:
            data = list(data)
            count = 0
            for i in data:
                if i == ' ':
                    count = count+1
            orglen = len(data)
            mylen = count * 2 + len(data)
            for _ in range(len(data),mylen):
                data.append(' ')

            for strNow in range(orglen-1,-1,-1):
                if data[strNow] == ' ':
                    data[mylen-3:mylen] = '%20'
                    mylen = mylen - 3
                else:
                    data[mylen-1] = data[strNow]
                    mylen = mylen - 1
            print("".join(data))

    def testURLify_2(self):
        for k, data in enumerate(self.datas):
            for i in range(len(data)):
                if data[i] == ' ':
                    self.new_data[k].append('%20')
                else:
                    self.new_data[k].append(data[i])

            #print(''.join(self.new_data[k]))





if __name__ == "__main__":
    unittest.main()
