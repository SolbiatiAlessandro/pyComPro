class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.vectors = [(len(v), iter(v)) for v in (v2, v1) if v]

    def next(self):
        """
        :rtype: int
        """
        left, iterator = self.vectors.pop()
        if left > 1: self.vectors.insert(0, (left - 1, iterator))
        return iterator.next()
        
    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.vectors)

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
