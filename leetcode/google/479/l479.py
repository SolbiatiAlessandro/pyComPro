class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.vectors = [v1, v2]
        self.total = sum(len(v) for v in self.vectors)
        self.curr = 0
        self.vector_index, self.char_index = 0, 0

    def next(self):
        """
        :rtype: int
        """
        if not self.hasNext(): return None
        self.curr += 1

        def advance():
            self.vector_index = (self.vector_index + 1)
            if self.vector_index == len(self.vectors):
                self.vector_index = 0
                self.char_index += 1
        
        while self.char_index >= len(self.vectors[self.vector_index]):
            advance()
        res = self.vectors[self.vector_index][self.char_index]
        advance()
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.curr + 1 > self.total: return False
        return True

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
