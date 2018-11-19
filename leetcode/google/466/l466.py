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
        curr = sum(nums[i*2] for i in xrange(len(nums)/2 - 1) if i*2 < len(nums))
        res = curr
        for counter in xrange(len(nums)):
            print "\n"
            print curr
            index = (counter * 2) % (len(nums) - 1)
            print index, nums[index], nums[index - 2]
            curr += -nums[index] + nums[index - 2]
            print curr
            res = max(res, curr)
        return res
