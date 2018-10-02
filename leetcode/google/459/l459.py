class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = ord('a')
        bitmask = [-1]*30
        for i,c in enumerate(s):
            index = ord(c)-start
            if bitmask[index] == -1:
                bitmask[index] = i
            elif bitmask[index] > -1:
                bitmask[index] = -2
        res = 1e9
        for b in bitmask:
            if b > -1:
                res = min(res, b)
        return res if res != 1e9 else -1


