class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        answers = {}
        def solve(i, j):
            """recursive call for DP solution, i is index of word1, j index of word2"""
            if i < 0: return j + 1
            if j < 0: return i + 1
            if answers.get((i, j)) is None:
                if word1[i] == word2[j]: answers[(i, j)] = solve(i-1, j-1)
                else: answers[(i, j)] = min(solve(i-1,j), solve(i-1,j-1), solve(i,j-1)) + 1
            return answers[(i, j)]
        return solve(len(word1) - 1, len(word2) - 1)
