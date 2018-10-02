class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = ord('a')
        bitmaskAppear = [False]*30
        bitmaskRepeat = [False]*30
        for c in s:
            index = ord(c)-start
            if not bitmaskAppear[index]:
                bitmaskAppear[index] = True
            else:
                bitmaskRepeat[index] = True
        for i, c in enumerate(s):
            index = ord(c)-start
            if bitmaskAppear[index] and not bitmaskRepeat[index]:
                return i
        return -1

