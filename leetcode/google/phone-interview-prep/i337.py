class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        mask = [0 for _ in s]
        for word in dict:
            begin = 0
            index = s.find(word)
            if index == -1: continue
            while True:
                begin += index
                mask[begin:begin+len(word)] = [1]*len(word)
                index = s[begin + 1:].find(word) + 1
                if index == 0: break
        mask = [0] + mask + [0]

        added = 0
        for i in xrange(1, len(mask)):
            if mask[i] == 1 and mask[i-1] == 0:
                index = added + i - 1
                s = s[:index] + "<b>" + s[index:]
                added += 3
            elif mask[i] == 0 and mask[i - 1] == 1:
                index = added + i - 1
                s = s[:index] + "</b>" + s[index:]
                added += 4
        return s
        

if __name__ == "__main__":
    s = "abcxyz123"
    dict = ["abc","123"]
    _s=Solution()
    got = _s.addBoldTag(s,dict)
    assert got == "<b>abc</b>xyz<b>123</b>"
    s = "abcxyz123uuuabcuuuuuabcuuuuu"
    dict = ["abc","123"]
    _s=Solution()
    _s.addBoldTag(s,dict)

    s = "aaabbcc"
    dict = ["aaa","aab","bc"]
    got = _s.addBoldTag(s,dict)
    assert got == "<b>aaabbc</b>c"

    s = "a"
    dict = []
    got = _s.addBoldTag(s,dict)
    assert got == "a"

    print "ok"

