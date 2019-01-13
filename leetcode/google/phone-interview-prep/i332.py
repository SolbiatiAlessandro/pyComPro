class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if k == 0: return 0
        substring = {}
        start, end = 0, 0
        while len(substring) < k and end < len(s):
            end += 1
            if substring.get(s[end - 1]): substring[s[end - 1]] += 1
            else: substring[s[end - 1]] = 1
        if len(substring) < k: return len(s)
        res = end - start
        while end < len(s):
            end += 1
            if substring.get(s[end - 1]): substring[s[end - 1]] += 1
            else: substring[s[end - 1]] = 1
            while len(substring) > k:
                substring[s[start]] -= 1
                if substring[s[start]] == 0: del substring[s[start]]
                start += 1
            res = max(res, end - start)
        return res

if __name__ == "__main__":
    s=Solution()
    got = s.lengthOfLongestSubstringKDistinct("eceba", 2)
    assert got == 3
    got = s.lengthOfLongestSubstringKDistinct("aa", 1)
    assert got == 2
    got = s.lengthOfLongestSubstringKDistinct("", 1)
    assert got == 0
    got = s.lengthOfLongestSubstringKDistinct("a", 1)
    assert got == 1
    got = s.lengthOfLongestSubstringKDistinct("aba", 1)
    assert got == 1
    got = s.lengthOfLongestSubstringKDistinct("a", 0)
    assert got == 0
    got = s.lengthOfLongestSubstringKDistinct("abcdefg", 3)
    assert got == 3
    got = s.lengthOfLongestSubstringKDistinct("aaaabcdefg", 3)
    assert got == 6
    got = s.lengthOfLongestSubstringKDistinct("abcdefgggg", 3)
    assert got == 6
    print "ok"
