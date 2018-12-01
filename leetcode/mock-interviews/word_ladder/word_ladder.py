class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        distances = [1e9 for _ in wordList]
            
        def one_difference(word1, word2):
            cnt = 0
            for index, char in enumerate(word1):
                if char != word2[index]: cnt += 1
                if cnt > 1: return False
            if cnt == 1: return True
            return False
        
        def compute_distances_from(index):
            distance = distances[index]
            compare_word = wordList[index]
            updated = []
            for i, word in enumerate(wordList):
                if i != index and one_difference(word, compare_word):
                    if distance + 1 < distances[i]:
                        distances[i] = distance + 1
                        updated.append(i)
            for i in updated:
                compute_distances_from(i)
        
        try:
            end_index = wordList.index(endWord)
            distances[end_index] = 1
            compute_distances_from(end_index)
        except ValueError as e:
            return 0
        
        res = 1e9
        for i, word in enumerate(wordList):
            if one_difference(beginWord, word):
                res = min(res, distances[i] + 1)
        return res if res != 1e9 else 0
