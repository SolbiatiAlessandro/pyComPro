class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        def get_bitmask(word):
            bitmask = 0
            for letter in word:
                bitmask |= 1 << (ord(letter)-97)
            return bitmask
        res, bitmasks = 0, [get_bitmask(word) for word in words]
        for index, bitmask in enumerate(bitmasks):
            for iterate in xrange(index, len(bitmasks)):
                if not bitmask & bitmasks[iterate]:
                    res = max(len(words[index]) * len(words[iterate]), res)
        return res
