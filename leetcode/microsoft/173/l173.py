from bisect import bisect

class Solution(object):
    def twoSum(self, nums, target):
        """ solution based on target = a + b
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = sorted([(num, index) for index, num in enumerate(nums)])
        for i, a in enumerate(nums):
            b = target - a[0]
            j = bisect(nums, (b, len(nums)))
            if j > 0 and nums[j - 1][0] == b:
                return min(a[1], nums[j - 1][1]), max(a[1], nums[j - 1][1]),
