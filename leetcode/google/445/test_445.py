import unittest
import l445
from l445 import Interval


class testSolution(unittest.TestCase):
    
    def setUp( self ):
        self.s = l445.Solution()
        self.s.intervals = [Interval(1,2),Interval(3,5),Interval(6,7),Interval(8,10),Interval(12,16)]

    def test_start(self):
        ss = l445.search_start

        # interval testing
        got = ss(self.s.intervals, 4)
        self.assertEqual(got, 2)
        got = ss(self.s.intervals, 2)
        self.assertEqual(got, 1)
        got = ss(self.s.intervals, 0)
        self.assertEqual(got, 0)
        got = ss(self.s.intervals, 7)
        self.assertEqual(got, 3)
        got = ss(self.s.intervals, 10)
        self.assertEqual(got, 4)
        got = ss(self.s.intervals, 15)
        self.assertEqual(got, 5)

        # tricky, test coincident matching
        got = ss(self.s.intervals, 6)
        self.assertEqual(got, 2)
        got = ss(self.s.intervals, 1)
        self.assertEqual(got, 0)
        print "ok"
        for index, interval in enumerate(self.s.intervals):
            got = ss(self.s.intervals, interval.start)
            self.assertEqual(got, index)

    def test_end(self):
        ss = l445.search_end

        # interval testing
        got = ss(self.s.intervals, 4)
        self.assertEqual(got, 0)
        got = ss(self.s.intervals, 2)
        self.assertEqual(got, 0)
        got = ss(self.s.intervals, 0)
        self.assertEqual(got, -1)
        got = ss(self.s.intervals, 7)
        self.assertEqual(got, 2)
        got = ss(self.s.intervals, 10)
        self.assertEqual(got, 3)
        got = ss(self.s.intervals, 15)
        self.assertEqual(got, 3)

    def test_end_coincident(self):
        ss = l445.search_end

        # tricky, test coincident matching
        got = ss(self.s.intervals, 6)
        self.assertEqual(got, 1)
        got = ss(self.s.intervals, 1)
        self.assertEqual(got, -1)
        for index, interval in enumerate(self.s.intervals):
            got = ss(self.s.intervals, interval.end)
            self.assertEqual(got, index)
        print "ok"


    def test_solution( self ):
        intervals = [Interval(1,3),Interval(6,9)]
        newInterval = Interval(2,5)
        got = self.s.insert(intervals, newInterval)
        expected = [[1,5],[6,9]]
        for i, interval in enumerate(got):
            self.assertEqual(interval.start,expected[i][0])
            self.assertEqual(interval.end,expected[i][1])

        intervals = [Interval(1,2),Interval(3,5),Interval(6,7),Interval(8,10),Interval(12, 16)]
        newInterval = Interval(4,8)
        got = self.s.insert(intervals, newInterval)
        expected = [[1,2],[3,10],[12,16]]
        for i, interval in enumerate(got):
            self.assertEqual(interval.start,expected[i][0])
            self.assertEqual(interval.end,expected[i][1])

        intervals = [Interval(1,2),Interval(3,5),Interval(6,7),Interval(8,10),Interval(12, 16)]
        newInterval = Interval(-2,8)
        got = self.s.insert(intervals, newInterval)
        expected = [[-2,10],[12,16]]
        for i, interval in enumerate(got):
            self.assertEqual(interval.start,expected[i][0])
            self.assertEqual(interval.end,expected[i][1])

        intervals = [Interval(1,2),Interval(3,5),Interval(6,7),Interval(8,10),Interval(12, 16)]
        newInterval = Interval(-2,18)
        got = self.s.insert(intervals, newInterval)
        expected = [[-2,18]]
        for i, interval in enumerate(got):
            self.assertEqual(interval.start,expected[i][0])
            self.assertEqual(interval.end,expected[i][1])

        intervals = [Interval(1,2),Interval(3,5),Interval(6,7),Interval(8,10),Interval(12, 16)]
        newInterval = Interval(7,12)
        got = self.s.insert(intervals, newInterval)
        expected = [[1,2],[3,5],[6,16]]
        for i, interval in enumerate(got):
            self.assertEqual(interval.start,expected[i][0])
            self.assertEqual(interval.end,expected[i][1])

        intervals = [Interval(1,2),Interval(3,5),Interval(6,7),Interval(8,10),Interval(12, 16)]
        newInterval = Interval(7,10)
        got = self.s.insert(intervals, newInterval)
        expected = [[1,2],[3,5],[6,10],[12,16]]
        for i, interval in enumerate(got):
            self.assertEqual(interval.start,expected[i][0])
            self.assertEqual(interval.end,expected[i][1])

        intervals = []
        newInterval = Interval(7,10)
        got = self.s.insert(intervals, newInterval)
        expected = [[7,10]]
        for i, interval in enumerate(got):
            self.assertEqual(interval.start,expected[i][0])
            self.assertEqual(interval.end,expected[i][1])

        print "okok"
        

if __name__ == "__main__":
    unittest.main()

