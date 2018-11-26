class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        total_max, total_min = -1e9, 1e9
        for _list in nums:
            for num in _list:
                total_max, total_min = max(num, total_max), min(num, total_min)
        shift, indexes = total_min, [set() for _ in xrange(total_min, total_max + 1)]
        
        print indexes
        
        for list_index, _list in enumerate(nums):
            for num in _list:
                indexes[num - shift].add(list_index)
                
        i, included = 0, dict() # this is a bitmask that keep track of included indexes
        while len(included) < len(nums): # while they are not all included TODO
            for list_index in indexes[i]:
                if included.get(list_index) is not None:
                    included[list_index] += 1
                else:
                    included[list_index] = 1
            i += 1
            
        start = 0
        advance_start = True
        while advance_start and start < i:
            for list_index in indexes[start]:
                if included[list_index] - 1 == 0:
                    advance_start = False
                    break
            if advance_start:
                start += 1
                for list_index in indexes[start]:
                    included[list_index] -= 1
        min_res, res = i - start, [start - shift, i - 1 - shift]
        
        
        print [res[0] + 2*shift, res[1] + 2*shift]
        for end in xrange(i, len(indexes)):
            for list_index in indexes[end]:
                included[list_index] += 1
            advance_start = True
            while advance_start and start < end:
                for list_index in indexes[start]:
                    if included[list_index] - 1 == 0:
                        advance_start = False
                        break
                if advance_start:
                    start += 1
                    for list_index in indexes[start]:
                        included[list_index] -= 1
            if end - start < min_res:
                res = [start - shift, end - shift]
                #min_res = res[1] - res[0]
            print [res[0] + 2*shift, res[1] + 2*shift]
        
        return res[0] + 2*shift, res[1] + 2*shift
             
            
            
            
            
            
                
            
        
        
        
            
        
        
