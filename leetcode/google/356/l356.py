
class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        #print "\n"
        end, left, res = cols - 1, rows, 0
        precomputed = [None] * (cols + 1)

        def compute(start):
            """computes in a DP fashion how many lines it takes 
            to write all words in senteces, return lines and end"""
            #print "call compute "+str(start)
            if precomputed[start] is not None:
                return precomputed[start]
            height, index = 0, start
            for word in sentence:
                if index + len(word) + 1 > cols:
                    index = len(word)
                    height += 1
                else:
                    index += len(word) + 1
                #print word, index
            precomputed[start] = (index, height)
            #print index, height
            return index, height

        total_len = sum([len(word) for word in sentence]) + len(sentence)
        while left >= 0:
            start = end
            res += (cols - start) / total_len
            start += ((cols - start) / total_len) * total_len
            res += 1
            end, height = compute(start)
            left -= height
        return res - 1
