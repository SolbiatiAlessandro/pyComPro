class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        i = 0
        intervals.sort(key = lambda x: x.start)
        while i < len(intervals) - 1:
            if intervals[i].end >= intervals[i + 1].start:
                intervals[i].end = max(intervals[i + 1].end,
                                        intervals[i].end)
                del intervals[i + 1]
            else: i += 1
        return intervals
        

        
