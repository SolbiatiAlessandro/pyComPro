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
        shift = total_min
        for list_index, _list in enumerate(nums):
            for num in _list:
                indexes[num - shift].add(list_index)

        start, end, included = set(), 0, -1
        while len(included) < len(nums):
            end += 1
            included = included.union(indexes[end])

        from heapq import heappush
        heap = []

        for list_indexes in indexes:
            if list_indexes:

                
