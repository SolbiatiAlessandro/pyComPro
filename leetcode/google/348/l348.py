class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        answers = {}
        def solve(string):
            if string == "": return True
            if answers.get(string) is None:
                answers[string] = any([solve(string[len(word):]) for word in wordDict if string[:len(word)] == word])
            return answers[string]
        return solve(s)
