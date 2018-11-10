import bisect

class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        #import pdb;pdb.set_trace()
        res, nums_with_index = [], sorted(zip(nums, range(len(nums))))
        for query in findNums:
            index = bisect.bisect(nums_with_index, (query, -1))
            original_index = nums_with_index[index][1]
            found = False
            for num in nums[original_index:]:
                if num > query:
                    res.append(num)
                    found = True
                    break
            if not found: res.append(-1)
        return res
            

        
