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
    matches, matches_count = defaultdict(list), 0
    res, start, end = 0, -1, -1
    for index, num in enumerate(nums):
        matches[num + distance].append(index)
        if matches[num]:
            matches_count += len(matches[num])
            a, b = matches[num][0], index  # a, b: new segment extremes
            if start == -1:                          # first segment
                res += int((b - a)*(b - a + 1)/2)  # add new segment
                start, end = a, b
            elif not (start <= a and end >= b):     # if new segment
                res += int((b - a)*(b - a + 1)/2)  # add new segment
                if a < end:                  # subtract intersection
                    res -= int((end - a)*(end - a + 1)/2)
            end = b
    return res - matches_count if matches_count < res else 0, res


class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
