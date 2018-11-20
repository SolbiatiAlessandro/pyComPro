class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answers = {}
        def solve(start, end):
            if start > end: return 0
            if start == end: return nums[start]
            if answers.get((start, end)) is None:
                answers[(start, end)] = max(nums[start] + solve(start + 2, end), solve(start + 1, end))
            return answers[(start, end)]
        return max(solve(0, len(nums) - 2), solve(1, len(nums) - 1)) if len(nums) != 1 else nums[0]
