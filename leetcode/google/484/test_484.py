import unittest
import l484


class testSolution(unittest.TestCase):
    
    def setUp( self ):
        self.s = l484.Solution()

    def test_solution( self ):
        got = self.s.numberOfPatterns(1, 1)
        self.assertEqual(got, 9)
        got = self.s.numberOfPatterns(1, 2)
        self.assertEqual(got, 65)


if __name__ == "__main__":
    unittest.main()
