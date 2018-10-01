def prefixFunction(string):
    """
    given a string the function generate the array with 
    prefix function, defined as longest prefix that is 
    also suffix of the given substring.
    Note: on CLRS (pg. 926 ) the prefixFunction is 1 base,
    here is 0 based

    :string (str) input string
    :rtype (list[int]) return the prefix function 
    """
    k,prefixArray=0,[0] 
    for q in xrange(1, len(string)):
        while k>0 and string[k]!=string[q]:
            k=prefixArray[k-1]
        if string[k]==string[q]:
            k=k+1
        prefixArray.append(k)
    return prefixArray

def longestPalindrome(string):
    """
    :string (str) string input
    :rtype (int) the size of the longest palindrome starting from 0
    compute in O(n) the longest palindrome using KMP implementation
    """
    prefixArray, i = prefixFunction(string), 0
    for j in reversed(xrange(len(string))):
        while i > 0 and string[i] != string[j]:
            i = prefixArray[i-1]
        if string[i] == string[j]:
            i += 1
        if i == j or j - i == 1:
            return i+j
    return 1 if len(string)>0 else 0

class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = longestPalindrome(s)
        return s[:-(len(s)-l+1):-1] + s
