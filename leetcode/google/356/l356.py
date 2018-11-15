class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        end, left, res = cols - 1, rows, 0
        precomputed = [None] * cols

        def compute(start):
            """computes in a DP fashion how many lines it takes 
            to write all words in senteces, return lines and end"""
            if precomputed[start] is not None:
                return precomputed[start]
            height, index = 0, start
            for word in sentence:
                if index + len(word) + 1 >= cols:
                    index = len(word)
                    height += 1
                else:
                    index += len(word) + 1
            precomputed[start] = (index, height)
            return index, height

        while left >= 0:
            res += 1
            start = end
            end, height = compute(start)
            left -= height
        return res - 1
