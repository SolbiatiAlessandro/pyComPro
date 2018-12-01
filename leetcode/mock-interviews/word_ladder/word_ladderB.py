from collections import defaultdict

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        class distances(dict):
            def __missing__(self, key):
                return 1e9

        groups, distance = defaultdict(list), distances()
        for word in wordList:
            for i, _ in enumerate(word):
                groups[(word[:i],word[i+1:])].append(word)

        if endWord not in wordList: return 0

        stack = [(endWord, 1)]
        while stack:
            word, step = stack.pop()
            for i, _ in enumerate(word):
                key = (word[:i],word[i+1:])
                if step < distance[key]:
                    distance[key] = min(distance[key], step)
                    for next_word in groups[(word[:i],word[i+1:])]:
                        if next_word != word:
                            stack.insert(0, (next_word, step + 1))

        res = 1e9
        for i, _ in enumerate(beginWord):
            res = min(res, distance[(beginWord[:i],beginWord[i+1:])])
        return res + 1 if res != 1e9 else 0
