class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import defaultdict
        self.table = defaultdict(int)
        self.counter = 0
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        self.counter += 1
        for i, char in enumerate(word):
            self.table[(i, char)] |= 1 << self.counter
            self.table[(i, '.')] |= 1 << self.counter
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        res = None
        for i, char in enumerate(word):
            if res is None:
                res = self.table[(i, char)]
            else:
                res &= self.table[(i, char)]
        return res != 0
        


# Your WordDictionary object will be instantiated and called as such:
if __name__ == "__main__":
    obj = WordDictionary()
    obj.addWord('aaa')
    assert obj.search("..a")
    assert obj.search("a.a")
    assert obj.search("aaa")
    assert not obj.search("ba.")
    assert not obj.search("aa..")
