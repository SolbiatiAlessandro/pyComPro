class Node(object):
    """this is the node of suffix/prefix trie"""
    def __init__(self, letter, height, parent, index):
        self.letter = letter
        self.children = dict()
        self.parent = parent
        self.height = height
        self.index = index

    def _print(self):
        print self.letter, self.height, self.index
        for _, child in self.children.items():
            child._print()


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2: return s
        tree, max_length, res = Node('*', 0, None, -1), 0, ""
        for i in reversed(xrange(len(s))):
            curr = tree
            #print s[i:]
            for k in xrange(i, len(s)):
                letter = s[k]
                if curr.children.get(letter) is None:
                    curr.children[letter] = Node(letter,
                                                 curr.height+1, curr, k)
                curr = curr.children[letter]
        #tree._print()
        #import pdb;pdb.set_trace() 
        for i in xrange(len(s)):
            curr = tree
            #print s[i::-1]
            for letter in s[i::-1]:
                if curr.children.get(letter) is None:
                    break
                curr = curr.children[letter]
                if curr.height > max_length and curr.index == i:
                    max_length = curr.height
                    res, recurse = "", curr
                    while recurse is not None:
                        res += recurse.letter
                        recurse = recurse.parent

        #print res+"\n"
        return res[:-1] if len(res) > 0 else res[0]
