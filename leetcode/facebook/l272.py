def isBadVersion(n):
    global array
    return array[n - 1]

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        a, b = 1, n
        while b >= a:
            m = (b-a)/2 + a
            this = isBadVersion(m)
            prev = isBadVersion(m - 1) if m > 1 else 0
            if this == True and prev == False: return m
            if this == True and prev == True: b = m
            if this == False: a = m + 1

if __name__ == "__main__":
    s = Solution()
    global array
    array = [0,0,0,1,1]
    assert s.firstBadVersion(5) == 4
    array = [0,0,0,0,1]
    assert s.firstBadVersion(5) == 5
    array = [1,1,1,1,1]
    assert s.firstBadVersion(5) == 1
    array = [1]
    assert s.firstBadVersion(1) == 1
    array = [0, 1]
    assert s.firstBadVersion(2) == 2
    print "ok"
