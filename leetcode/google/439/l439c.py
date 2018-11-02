from collections import defaultdict


def compute_range(nums, distance):
    """
    compute how many distances are smaller then distance
    and how many distances are equal to distance, among all
    possible distances in nums

    Arg:
        distance : (int), the distance to query
    Returns:
        first, last : indexes of first (inclusive) and last
        (exclusive) element equal to distance in the sorted
        list of distances in nums: [first, last)
    """
    less, equal = 0, 0
    low, high = 0, - 1
    for i, num in enumerate(nums):

        less += low - i - 1
        while low < len(nums) - 1 and nums[low + 1] - distance < num:
            less += 1
            low += 1
        if nums[low] - distance == num:
            equal += 1
        while low < len(nums) - 1 and nums[low + 1] - distance == num:
            equal += 1
            low += 1

        while high < len(nums) - 1 and nums[high + 1] + distance < num:
            high += 1
        if nums[high] + distance == num:
            equal += 1
        while high < len(nums) - 1 and nums[high + 1] + distance == num:
            high += 1
            equal += 1
        less += i - high

    return max(0, less/2), less/2 + equal/2


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
