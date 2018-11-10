import bisect

class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        #import pdb;pdb.set_trace()
        res = []
        answers = dict()
        for query in findNums:
            original_index = nums.index(query)
            found = False
            for num in nums[original_index:]:
                num_answer = answers.get(num)
                if num_answer > query:
                    res.append(num_answer)
                    answers[query] = num_answer
                    found = True
                    break
                if num > query:
                    res.append(num)
                    answers[query] = num
                    found = True
                    break
            if not found: res.append(-1)
        return res
            

        
