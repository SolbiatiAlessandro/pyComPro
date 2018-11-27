import unittest
import smallest_range


class testSolution(unittest.TestCase):
    
    def setUp( self ):
        self.s = smallest_range.Solution()

    def test_solution( self ):
        nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
        got = self.s.smallestRange(nums)
        self.assertEqual(got, [20, 24])
        

if __name__ == "__main__":
    unittest.main()

