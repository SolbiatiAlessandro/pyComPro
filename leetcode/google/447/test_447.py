import unittest
import l447


class testSolution(unittest.TestCase):
    
    def setUp( self ):
        self.s = l447.Solution()

    def test_solution( self ):
        nums1 = [1,7,11]
        nums2 = [2,4,6]
        k = 3
        
        got = self.s.kSmallestPairs(nums1, nums2, k)
        self.assertEqual(got, [[1,2],[1,4],[1,6]] )

        
if __name__ == "__main__":
    unittest.main()

