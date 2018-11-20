class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answers = {}
        def solve(visited, pos):
            if pos == len(nums): return 0
            if answers.get((visited, pos)) is None:
                if not (visited & 1 << (pos + 1)%len(nums)) and not (visited & 1 << (pos - 1)):
                    answers[(visited, pos)] = max(solve(visited|1<<(pos), pos + 1) + nums[pos], solve(visited, pos + 1))
                else: answers[(visited, pos)] = solve(visited, pos + 1)
            return answers[(visited, pos)]
        return max(solve(0, 1), solve(1, 1) + nums[0]) if nums else 0
