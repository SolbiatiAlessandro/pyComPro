import unittest
import l440


class testSolution(unittest.TestCase):
    
    def setUp( self ):
        self.s = l440.Solution()

    def test_solution( self ):
        
        nums1 = [1,2,2,1]
        nums2 = [2,2]
        self.assertEqual( self.s.intersection( nums1, nums2 ), [2] )
        nums1 = [4,9,5]
        nums2 = [9,4,9,8,4]
        self.assertEqual( self.s.intersection( nums1, nums2 ), [9,4] )
        nums1 = []
        nums2 = []
        self.assertEqual( self.s.intersection( nums1, nums2 ), [] )


        
if __name__ == "__main__":
    unittest.main()

