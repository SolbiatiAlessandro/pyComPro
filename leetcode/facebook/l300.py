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
        l = len(word)
        for i, char in enumerate(word):
            self.table[(l, i, char)] |= 1 << self.counter
            self.table[(l, i,  '.')] |= 1 << self.counter
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        res = None
        l = len(word)
        for i, char in enumerate(word):
            if res is None:
                res = self.table[(l, i, char)]
            else:
                res &= self.table[(l, i, char)]
        return res != 0