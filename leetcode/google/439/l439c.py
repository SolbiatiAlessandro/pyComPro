from collections import defaultdict


def compute_range(nums, distance):
    """
    compute how many distances are smaller then distance
    and how many distances are equal to distance, among all
    possible distances in nums, time complexity O(len(nums)^2)

    Arg:
        distance : (int), the distance to query
    Returns:
        first, last : zero-based indexes of first (inclusive) and last
        (exclusive) element equal to distance in the sorted
        list of distances in nums: [first, last)
    """
    less, equal = 0, 0
    for i, num in enumerate(nums):
        for high in xrange(0, i):
            if nums[high] + distance > num:
                less += 1
            elif nums[high] + distance == num:
                equal += 1
        for low in xrange(i + 1, len(nums)):
            if nums[low] - distance < num:
                less += 1
            elif nums[low] - distance == num:
                equal += 1
    return max(0, less/2), less/2 + equal/2

def compute_range_fast(nums, distance):
    """
    compute how many distances are smaller then distance
    and how many distances are equal to distance, among all
    possible distances in nums, time complexity O(len(nums))

    Arg:
        distance : (int), the distance to query
    Returns:
        first, last : zero-based indexes of first (inclusive) and last
        (exclusive) element equal to distance in the sorted
        list of distances in nums: [first, last)
    """
    less, equal = 0, 0
    a, b = 0, 0  # a, b are the extremes of the segment of less distances
    c, d = 0, 0  # c, d are the extremes of the segment of less/equal distances
    for i in xrange(len(nums) - 1):
        num = nums[i]
        while c < len(nums) and nums[c] + distance < num: c += 1
        a = c
        while a < len(nums) and nums[a] + distance == num: a += 1
        while b < len(nums) - 1 and nums[b + 1] - distance < num: b += 1
        d = b
        while d < len(nums) - 1 and nums[d + 1] - distance == num: d += 1

        less += b - a
        equal += d - c

    return max(0, less/2), equal/2

class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        k -= 1
        nums.sort()
        b = nums[-1] - nums[0]
        a = min([nums[i+1] - nums[i] for i in xrange(len(nums) - 1)])
        while True:
            m = (b-a)/2 + a
            start, end = compute_range(nums, m)
            if start <= k < end:
                return m
            elif k >= end:
                a = m + 1
            else:
                b = m - 1
