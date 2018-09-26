class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        chk = [ch.lower() for ch in s if ch.isalnum()]
        return chk == chk[::-1]
