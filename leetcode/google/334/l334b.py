class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        answers = dict()
        def compute_answer(string):
            if string == '0': return 0
            if len(string) <= 1: return 1
            if answers.get(string) is not None: return answers[string]
            answer = 0
            if string[0] != '0':
                answer += compute_answer(string[1:])
                if int(string[:2]) < 27: answer += compute_answer(string[2:])
            answers[string] = answer
            return answer
        return compute_answer(s)
