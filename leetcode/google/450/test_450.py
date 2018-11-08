import unittest
import l450


class testSolution(unittest.TestCase):
    
    def setUp( self ):
        self.s = l450.Solution()

    def test_solution( self ):
        from l450 import Interval
        test_input = [Interval(1,3),Interval(2,6),Interval(8,10),Interval(15,18)]
        expected = [[1,6],[8,10],[15,18]]
        got = self.s.merge(test_input)
        for i,interval in enumerate(got):
            self.assertEqual(interval.end, expected[i][1])
            self.assertEqual(interval.start, expected[i][0])
        
        test_input = [Interval(1,4),Interval(4,5)]
        expected = [[1,5]]
        got = self.s.merge(test_input)
        for i,interval in enumerate(got):
            self.assertEqual(interval.end, expected[i][1])
            self.assertEqual(interval.start, expected[i][0])

        test_input = [Interval(1,4)]
        expected = [[1,4]]
        got = self.s.merge(test_input)
        for i,interval in enumerate(got):
            self.assertEqual(interval.end, expected[i][1])
            self.assertEqual(interval.start, expected[i][0])

        test_input = []
        expected = []
        got = self.s.merge(test_input)
        for i,interval in enumerate(got):
            self.assertEqual(interval.end, expected[i][1])
            self.assertEqual(interval.start, expected[i][0])

        test_input = [Interval(1,3),Interval(2,6),Interval(1,10),Interval(-5,18)]
        expected = [[-5,18]]
        #import pdb;pdb.set_trace()
        got = self.s.merge(test_input)
        for i,interval in enumerate(got):
            self.assertEqual(interval.end, expected[i][1])
            self.assertEqual(interval.start, expected[i][0])

        test_input = [Interval(1,4),Interval(0,4)]
        expected = [[0,4]]
        got = self.s.merge(test_input)
        for i,interval in enumerate(got):
            self.assertEqual(interval.end, expected[i][1])
            self.assertEqual(interval.start, expected[i][0])


        


if __name__ == "__main__":
    unittest.main()

