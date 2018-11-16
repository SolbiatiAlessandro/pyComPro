class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        #print "\n"
        end, left, res = cols - 1, rows, 0
        precomputed = [None] * (cols + 1)
        first_seen = [None] * (cols + 1)

        def compute(start):
            """returns (index at the end of the shift),
            (how many time it repeated the sentece), (how many lines it went down)"""
            print "call compute "+str(start)
            if first_seen[start] is None:
                first_seen[start] = res, left
            else:
                prev_res, prev_left = first_seen[start]
                precomputed[start] = res - prev_res, left - prev_left

            if precomputed[start] is not None:
                return start, precomputed[start][0], precomputed[start][1]

            height, index = 0, start
            for word in sentence:
                if index + len(word) + 1 > cols:
                    index = len(word)
                    height += 1
                else:
                    index += len(word) + 1
                #print word, index
            return index, 1, height

        while left >= 0:
            start = end
            end, repeat, height = compute(start)
            print end, repeat, height
            left -= height
            res += repeat
        return res - 1
