def small_division(dividend, divisor):
    curr, res = 0, 0
    while curr + divisor <= dividend:
        curr += divisor
        res += 1
    return res, dividend - curr

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = 1 if dividend * divisor > 0 else -1
        dividend, divisor = abs(dividend), abs(divisor)
        
        dividend = str(dividend)
        if len(dividend) > 1:
            res, carry = "", dividend[0]

            for i in xrange(1, len(dividend)):
                carry += dividend[i]
                _res, _carry = small_division(int(carry), divisor)
                carry = str(_carry)
                res += str(_res)
        else:
            res = small_division(int(dividend), divisor)[0]

        res = (sign * int(res)) if res else 0
        res = max(-pow(2, 31), res)
        res = min(pow(2, 31) - 1, res)
        return res 
            
            
if __name__ == "__main__":
    assert small_division(11, 3) == (3, 2)
    assert small_division(2,  3) == (0, 2)
    assert small_division(4,  3) == (1, 1)
    assert small_division(6,  3) == (2, 0)
    assert small_division(51,  5) == (10, 1)
    s = Solution()
    assert s.divide(510, 5) == 102
    assert s.divide(4, 5) == 0
    assert s.divide(500, 5) == 100
    assert s.divide(173, 5) == 34
    assert s.divide(10, -3) == -3
    assert s.divide(7, -3) == -2
    assert s.divide(-7, -3) == 2
    assert s.divide(-7, 3) == -2
    assert s.divide(9, 3) == 3
    assert s.divide(1, 1) == 1
    assert s.divide(3, 3) == 1
    assert s.divide(8, 3) == 2
    assert s.divide(7, 3) == 2

