def digits_to_int(digits):
    string = "".join(map(str, digits))
    return int(string)

def int_to_digits(num):
    return list(map(int, str(num)))
    
class Solution(object):
    def plusOne(self, digits):
        num = digits_to_int(digits)
        return int_to_digits(num + 1)

if __name__ == "__main__":

    num, digits = 100, [1,0,0]
    assert int_to_digits(num) == digits
    assert digits_to_int(digits) == num

    num, digits = 0, [0]
    assert int_to_digits(num) == digits
    assert digits_to_int(digits) == num

    num, digits = 132, [1,3,2]
    assert int_to_digits(num) == digits
    assert digits_to_int(digits) == num

    s = Solution()
    assert s.plusOne([1,2,3]) == [1,2,4]
    assert s.plusOne([1,9,9]) == [2,0,0]
    assert s.plusOne([0]) == [1]
