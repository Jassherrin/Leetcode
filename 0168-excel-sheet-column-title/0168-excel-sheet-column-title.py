class Solution(object):
    def convertToTitle(self, columnNumber):
        res = ""

        while columnNumber > 0:
            offset = (columnNumber - 1) % 26
            res += chr(ord('A')+offset)
            columnNumber = (columnNumber - 1) // 26

        return res[::-1]
        