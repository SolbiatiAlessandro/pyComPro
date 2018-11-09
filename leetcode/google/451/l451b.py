class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res, max_len = [""], [0]
        def expand(start, end):
            while start >= 0 and end < len(s) and s[start] == s[end]:
                if end - start + 1 > max_len[0]:
                    max_len[0] = end - start + 1
                    res[0] = s[start:end+1]
                start -= 1
                end += 1

        for i in xrange(len(s)):
            expand(i, i)
            expand(i, i + 1)

        return res[0]
