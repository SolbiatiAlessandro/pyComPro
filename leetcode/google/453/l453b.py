class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        stack, res = [nums[0]], {}
        for i in xrange(1, len(nums)):
            while stack and nums[i] > stack[-1]:
                res[stack.pop()] = nums[i]
            if nums[i - 1] < nums[i]:
                res[nums[i - 1]] = nums[i]
            else:
                stack.append(nums[i])
        return [res[query] if res.get(query) else -1 for query in findNums ]
