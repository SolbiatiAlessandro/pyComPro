"""trying to replicate TLE heap solution,
I think is pretty interesting and I need to get familiar with heapq library"""
import heapq

class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        heap = [(nums[i+1] - nums[i], i, i+1)
                for i in xrange(len(nums) - 1)]
        heapq.heapify(heap)

        for _ in xrange(k):
            distance, list_number, list_index = heapq.heappop(heap)
            if list_index + 1 < len(nums):
                new_node = (nums[list_index + 1] - nums[list_number],
                            list_number, list_index + 1)
                heapq.heappush(heap, new_node)
        return distance
