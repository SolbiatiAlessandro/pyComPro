class Solution():
    def find_min(self, array):
        print array
        if array[-1] >= array[0]: return array[0]
        first = array[0]
        a, b = 0, len(array)
        while b > a:
            m = (b-a)/2 + a
            print a,b,m
            if m > 0 and array[m] < array[m - 1]: return array[m]
            elif array[m] > first:
                a = m + 1
            else:
                b = m - 1

if __name__ == "__main__":
    ss = Solution()
    array = [3,4,5,1,2]
    assert ss.find_min(array) == 1
