from math import ceil
from operator import truediv

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapping = dict()
        for i in xrange(26):
            mapping[str(i+1)] = chr(ord('A')+i)
        answers = dict()
        def compute_answer(string):
            if len(string) == 1: 
                return set(mapping.get(string))
            if len(string) == 2:
                return set(mapping.get(string), mapping.get(string[0]), mapping.get(string[1]))
            if answers.get(string) is not None: return answers[string]
            answer = set()
            for i in xrange(1, len(string)):
                answer.union(compute_answer(string[:i]))
                answer.union(compute_answer(string[i:]))
            answers[string] = answer
            return answer
        res = compute_answer(s)
        try: res.remove(None)
        except: pass
        return len(res)

