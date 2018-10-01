from suffixtree import suffix_array_ManberMyers, lcp_array

def longestPalindrome(string):
    """
    :string (str) string input
    :rtype (int) the size of the longest palindrome, (int) starting point
    of longest palindrome
    compute in O(nlogn) the longest palindrome using SuffixArray implementation 
    """
    l, maxLcp, maxLcpIndex = len(string), -1, -1
    reversedString = string+"$"+string[::-1]+"#"
    suffixArray = suffix_array_ManberMyers( reversedString )
    lcp = lcp_array( reversedString, suffixArray )
    import pdb;pdb.set_trace()
    for i in reversed(xrange(len(suffixArray))):
        if suffixArray[i] < l:
            if lcp[i] > maxLcp:
                maxLcp = lcp[i]
                maxLcpIndex = i
    return maxLcp, suffixArray[maxLcpIndex]


class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        NOT PASSING TESTS
        """
        longestPalindrome = 1
        substring = s[0] if len(s)>0 else ""
        letters = set(s[0]) if len(s)>0 else set()
        for i in xrange(1, len(s)):
            letters.add(s[i])
            substring+=(s[i])
            if len(letters)==1:
                longestPalindrome = i
            elif len(letters) <= (i/2)+1:
                if substring == substring[::-1]:
                    longestPalindrome = i
        #import pdb;pdb.set_trace()
        return s[:longestPalindrome:-1] + s





