class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mmin,mmax=1e9,0
        for num in nums:
            if num > 0:
                mmax = max(mmax, num)
                mmin = min(mmin, num)
        if mmin > 1:
            return 1
        helper = [False]*mmax
        for num in nums:
            if num>0:
                helper[num-1] = True
        for index, num in enumerate(helper):
            if not num:
                return index+1
        return mmax+1


