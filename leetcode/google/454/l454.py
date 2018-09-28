class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res,cnt = 0,0
        for c in nums:
            if c:
                cnt+=1
            else:
                res = max(cnt,res)
                cnt=0
        return max(cnt, res)
