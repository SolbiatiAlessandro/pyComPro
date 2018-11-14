import unittest
import l334b


class testSolution(unittest.TestCase):
    
    def setUp( self ):
        self.s = l334b.Solution()

    def test_solution( self ):
        got = self.s.numDecodings("12")
        self.assertEqual(got, 2)
        got = self.s.numDecodings("226")
        self.assertEqual(got, 3)
        got = self.s.numDecodings("100")
        self.assertEqual(got, 0)
        got = self.s.numDecodings("02")
        self.assertEqual(got, 0)
        got = self.s.numDecodings("10")
        self.assertEqual(got, 1)
        got = self.s.numDecodings("2234")
        self.assertEqual(got, 3)
        got = self.s.numDecodings("2214")
        self.assertEqual(got, 5)
        got = self.s.numDecodings("22635")
        got = self.s.numDecodings("226353")

    def test_two_solutions(self):
        import random
        import l334 
        benchmark = l334.Solution().numDecodings
        for length in xrange(10, 100):
            string = ''.join([str(int(random.random()*10)) for _ in xrange(length)])
            got = self.s.numDecodings(string)
            got_benchmark = benchmark(string)
            self.assertEqual(got, got_benchmark)
        print "benchmark test ok"
            


if __name__ == "__main__":
    unittest.main()

