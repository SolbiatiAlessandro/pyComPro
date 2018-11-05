class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1: return 1
        if x == 0: return 0
        from math import log
        a, b = log(x), x/2
        while True:
            m = int((b-a)/2 + a)
            if m*m <= x < (m+1)*(m+1): return m
            elif x < m*m: b = m - 1
            else: a = m + 1
