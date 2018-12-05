class Solution(object):
    def reorganizeString(self, S):
        count_letter = [[0, i] for i in xrange(25)]
        for char in S: count_letter[ord(char) - 97][0] += 1
        count_letter.sort(reverse=True)
        count_letter = [k for k in count_letter if k[0] > 0]
        res = [""]
        def decrease(index):
            res[0] += chr(count_letter[index][1] + 97)
            count_letter[index][0] -= 1
            if count_letter[index][0] == 0: del count_letter[index]
        print count_letter
        while len(count_letter) > 1:
            i = len(count_letter) - 1
            while i > 0:
                for _ in xrange(count_letter[i][0]):
                    decrease(i); decrease(i - 1)
                i -= 2
        print res[0]
        print count_letter
        if len(count_letter) == 1:
            if count_letter[0][0] != 1: return " "
            return chr(count_letter[0][1] + 97) + res[0]
        return res[0]
