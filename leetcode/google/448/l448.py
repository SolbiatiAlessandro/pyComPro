class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        def transform(num):
            return a*num*num + b*num + c

        flipped = [0]
        if a >= 0: flipped[0], a, b, c = 1, -a , -b, -c
        turning_point = (-float(b)/float(a))/2 if a else b*1e9
        
        res = []
        half_index = 0
        while half_index < len(nums):
            num = nums[half_index]
            if num >= turning_point: break
            res.append(transform(num))
            half_index += 1
        index = len(res) 
        for num in nums[half_index: ]:
            new_num = transform(num)
            while index > 0 and res[index - 1] >= new_num:
                index-=1
            res.insert(index, new_num)
        return map(lambda x: -x, res[::-1]) if flipped[0] else res
