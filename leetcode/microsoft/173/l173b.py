class Solution(object):
    def twoSum(self, nums, target):
        """ solution based on target = a + b
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        targets = {}
        for i, num in enumerate(nums):
            if targets.get(num) is not None:
                return targets[num], i
            targets[target - num] = i
