class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        cnt = 0
        for i, num in enumerate(nums):
            if not num:
                cnt+=1
            elif cnt:
                nums[i-cnt] = nums[i]
                nums[i] = 0
