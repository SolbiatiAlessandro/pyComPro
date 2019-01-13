class Solution(object):
    def trap(self, height, verbose=False):
        """
        :type height: List[int]
        :rtype: int
        """
        start, end, res = 0, len(height) - 1, 0
        if height: ml, mr = height[start], height[end]
        while end > start:
            if ml <= mr:
                start += 1
                ml= max(ml, height[start])
                res += ml - height[start]
            else:
                end -= 1
                mr = max(mr, height[end])
                res += mr - height[end]
            if verbose: print end, start, res
        return res


if __name__ == "__main__":
    s=Solution()
    nums = [1,0,2,1,0,1,3,2,1,2,1,1]
    got = s.trap(nums)
    assert got == 6
    got = s.trap(nums[::-1])
    assert got == 6
    nums = [1,0,2,1,0,1,4,2,1,2,4,1]
    got = s.trap(nums)
    assert got == 12
    nums = [2,1,0,2]
    got = s.trap(nums)
    assert got == 3
    nums = [1,2,3,4,3,2,1]
    got = s.trap(nums)
    assert got == 0
    nums = [2,1,0,1,2]
    got = s.trap(nums)
    assert got == 4
    print "ok"
