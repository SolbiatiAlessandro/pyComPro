class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        from collections import defaultdict
        letter_count = defaultdict(int)
        for char in S: letter_count[char] += 1
        total = sum(letter_count.values())
        letter_count = zip(letter_count.keys(), letter_count.values())
        letter_count.sort(key = lambda x : x[1], reverse = True)
        for i, (a, b) in enumerate(letter_count): letter_count[i] = [a, b]
        print letter_count, total
        for letter, count in letter_count:
            if count > (total - count) + 1: return " "
        res = ""
        for i in xrange(len(letter_count)):
            while letter_count[i][1] > 1:
                for j in xrange(i + 1, len(letter_count)):
                    if letter_count[j][0] > 0:
                        res += (letter_count[i][0])
                        letter_count[i][1] -= 1
                        res += (letter_count[j][0])
                        letter_count[j][1] -= 1
                        if letter_count[i][1] <= 1: break
            if letter_count[i][1] == 1:      
                res += letter_count[i][0]
                letter_count[i][1] -= 1
        print letter_count
        return res
