class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        letters, offset = set(), 0
        for i, c in enumerate(nums):
            if c in letters:
                offset += 1
            else:
                nums[i - offset] = nums[i]
                letters.add(c)
        return len(nums) - offset
        

        
