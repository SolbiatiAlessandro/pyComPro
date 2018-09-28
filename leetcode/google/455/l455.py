class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        NFprev, Fprev, res = 0, 0, 0
        for c in nums:
            if c:
                NF = NFprev + 1
                F = Fprev + 1
            else:
                NF = 0
                F = NFprev +1
            res = max( res, F, NF )
            NFprev = NF
            Fprev = F
        return res
