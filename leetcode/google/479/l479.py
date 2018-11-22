class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.vectors = [v1, v2]
        self.vector_indexes = []
        if v1: self.vector_indexes.insert(0, 0)
        if v2: self.vector_indexes.append(1)
        self.elem_indexes = [0, 0]
        self.index = 1

    def next(self):
        """
        :rtype: int
        """
        self.index = (self.index + 1) % len(self.vector_indexes) 
        index = self.vector_indexes[self.index]   # index of the vector
        vector = self.vectors[index]              # vector
        elem = vector[self.elem_indexes[index]]   # element from the vector
        self.elem_indexes[index] += 1
        if self.elem_indexes[index] == len(vector):
            del self.vector_indexes[self.index]   # if vector ended, delete it
        return elem

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.vector_indexes)

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
