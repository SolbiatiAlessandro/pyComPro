class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        #import pdb;pdb.set_trace()
        bitmask = [-1]*30
        for c in s:
            if not bitmask[ord(c)-ord('a')]:
                bitmask[ord(c)-ord('a')] = 1
            elif bitmask[ord(c)-ord('a')] == -1:
                bitmask[ord(c)-ord('a')] = 0
        for index, c in enumerate(s):
            if not bitmask[ord(c)-ord('a')]:
                return index
        return -1
