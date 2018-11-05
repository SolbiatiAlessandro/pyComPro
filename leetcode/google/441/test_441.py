import unittest
import l441


class testSolution(unittest.TestCase):
    
    def setUp( self ):
        self.s = l441.Solution()

    def test_solution( self ):

        got = self.s.mySqrt(101)
        self.assertEqual(got, 10)
        got = self.s.mySqrt(1)
        self.assertEqual(got, 1)
        got = self.s.mySqrt(0)
        self.assertEqual(got, 0)
        got = self.s.mySqrt(2)
        self.assertEqual(got, 1)

        import time
        import math
        longest = 0
        for x in xrange(int(10e5)):
            t1 = time.time()
            got = self.s.mySqrt(x)
            t2 = time.time()
            self.assertEqual(got, int(math.sqrt(x)))
            longest = max(t2 - t1, longest)
        print longest
            

if __name__ == "__main__":
    unittest.main()

