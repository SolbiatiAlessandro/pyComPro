class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

def search_start(intervals, start):
    """given a (int) start, binary searh the upper bound
    interval in intervals (m, m+1]"""
    if not intervals or start <= intervals[0].start: return 0
    if start > intervals[-1].start: return len(intervals)
    a, b = 0, len(intervals) - 1
    while True:
        m = (b - a)/2 + a
        if intervals[m].start < start <= intervals[m+1].start: return m+1
        elif start > intervals[m+1].start: a = m + 1
        else: b = m 


def search_end(intervals, end):
    """given a (int) start, binary searh the lower bound
    interval in intervals [m, m+1)"""
    if not intervals or end < intervals[0].end: return -1
    if end >= intervals[-1].end: return len(intervals) - 1
    a, b = 0, len(intervals) - 1
    while True:
        m = (b - a)/2 + a
        if intervals[m].end <= end < intervals[m+1].end: return m
        elif end >= intervals[m+1].end: a = m + 1
        else: b = m 

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        start_index =  search_start(intervals, newInterval.start)
        end_index = search_end(intervals, newInterval.end)

        if start_index > 0 and intervals[start_index - 1].end >= newInterval.start:
            start_index -= 1
            new_start = intervals[start_index].start
        else:
            new_start = newInterval.start
        if end_index < len(intervals) - 1 and intervals[end_index + 1].start <= newInterval.end:
            end_index += 1
            new_end = intervals[end_index].end
        else:
            new_end = newInterval.end

        del intervals[start_index: end_index + 1]
        intervals.insert(start_index, Interval(new_start, new_end))
        return intervals
