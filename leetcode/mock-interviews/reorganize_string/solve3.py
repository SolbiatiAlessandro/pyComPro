from collections import Counter

class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        counter = Counter(S)
        letters = sorted(zip(counter.values(), counter.keys()), reverse = True)
        res = [None for _ in xrange(len(S))]
        for count, letter in letters:
            index = 0
            while i < len(letters) and res[i] is not None: index += 1
            while count > 0:
                res[index] = letter
                index += 2
                count -= 1
        return res

        

