class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        k, cumsum, distance = k-1, 0, 1
        for cardinality in reversed(xrange(1, len(nums))):
            if cumsum <= k < cumsum + cardinality:
                break
            else:
                cumsum += cardinality
                distance += 1

        distances = sorted([abs(nums[x] - nums[x+distance]) 
                    for x in xrange(0, len(nums) - distance)])
        return distances[k - cumsum]
