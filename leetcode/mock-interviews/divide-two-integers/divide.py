class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor > dividend: return 0
        i = 0
        while (divisor << i) < dividend: i += 1
        return (1 << i) - self.divide((divisor << i) - dividend, divisor) - 1
