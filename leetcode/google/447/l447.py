import heapq

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        heap = [(num + nums2[0], index, 0)
                for index, num in enumerate(nums1)] if nums2 else []
        heapq.heapify(heap)

        res = []
        for _ in xrange(min(k, len(nums1)*len(nums2))):
            _, index_nums1, index_nums2 = heapq.heappop(heap)
            res.append([nums1[index_nums1], nums2[index_nums2]])
            if index_nums2 + 1 < len(nums2):
                new_node = (nums1[index_nums1] + nums2[index_nums2 + 1],
                            index_nums1, index_nums2 + 1)
                heapq.heappush(heap, new_node)

        return res
