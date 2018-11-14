import unittest
import l334


class testSolution(unittest.TestCase):
    
    def setUp( self ):
        self.s = l334.Solution()

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
        got = self.s.numDecodings("2263")
        got = self.s.numDecodings("22635")
        got = self.s.numDecodings("226353")
        


        

if __name__ == "__main__":
    unittest.main()

