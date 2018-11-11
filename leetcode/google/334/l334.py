from math import ceil
from operator import truediv

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        answers = dict()
        def compute_answer(string):
            if int(string) < 1: return 0
            if len(string) == 1: return 1
            if answers.get(string) is not None: return answers[string]
            answer = 0
            if int(string) < 27 and string[0] != "0": answer += 1
            for i in xrange(1, len(string)):
                first_answer = compute_answer(string[:i])
                second_answer = compute_answer(string[i:])
                answer += first_answer * second_answer
            for k in xrange(1, int(ceil(truediv(len(string), 2)))):
                answer -= abs((len(string)/k - 2))
            answers[string] = max(answer, 0)
            return max(answer, 0)
        return compute_answer(s)
