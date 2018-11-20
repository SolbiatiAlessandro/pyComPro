import operator

class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.max_size = size
        self.window = []
        self.curr_sum = 0

        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.window.insert(0, val)
        self.curr_sum += val
        if len(self.window) > self.max_size:
            self.curr_sum -= self.window.pop()
        return operator.truediv(self.curr_sum, len(self.window))

        
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
