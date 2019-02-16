class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        def match(i, j):
            if j == len(p) and i == len(s): return True
            if j >= len(p) or i >= len(s): return False
            if p[j] != '?' and p[j] != '*':
                return match(i+1, j+1) if s[i] == p[j] else False
            if p[j] == '?': return match(i+1, j+1)
            if p[j] == '*':
                for k in xrange(i, len(s) + 1):
                    if match(k, j+1): return True
            return False
        return match(0, 0)


if __name__ == "__main__":
    ss = Solution()
    s = "aa"
    p = "a"
    assert not ss.isMatch(s, p)
    s = "aa"
    p = "*"
    assert ss.isMatch(s, p)
    s = "adceb"
    p = "*a*b"
    assert ss.isMatch(s, p)
    s = "cb"
    p = "?a"
    assert not ss.isMatch(s, p)
    s = "acdcb"
    p = "a*c?b"
    assert not ss.isMatch(s, p)
