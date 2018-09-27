class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1,nums2,res = set(nums1),set(nums2),[]
        for n in nums1:
            if n in nums2:
                res.append(n)
        return res
