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
            #print string
            #import pdb;pdb.set_trace()
            if len(string) == 1: 
                return set([mapping.get(string)])
            if len(string) == 2:
                answer =  set([mapping.get(string)])
                if mapping.get(string[0]) and mapping.get(string[1]):
                    answer.add(mapping.get(string[0]) + mapping.get(string[1]))
                return answer
            if answers.get(string) is not None: return answers[string]
            answer = set()
            for i in xrange(1, len(string)):
                first_substring = compute_answer(string[:i])
                second_substring = compute_answer(string[i:])
                if first_substring and second_substring:
                    for first_match in first_substring:
                        for second_match in second_substring:
                            if first_match and second_match:
                                answer.add(first_match + second_match)
            answers[string] = answer
            try: res.remove(None)
            except: pass
            return answer
        res = compute_answer(s)
        #print s, res
        #print "\n\n"
        try: res.remove(None)
        except: pass
        return len(res)

