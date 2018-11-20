from collections import defaultdict

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not len(nums) % 2:
            even, odd = 0, 0
            for index, num in enumerate(nums):
                if index % 2: even += num
                else: odd += num
            return max(even, odd)
        if len(nums) == 1: return nums[0]
        curr = sum(nums[end] for end in map(lambda x : x * 2, xrange((len(nums) - 1)/2)))
        start, end = 0, 2*((len(nums) - 1)/2 - 1)
        res = curr
        for _ in xrange(len(nums)):
            curr -= nums[start]
            start, end = (start + 2)%len(nums), (end + 2)%len(nums)
            curr += nums[end]
            res = max(res, curr)
        return res
