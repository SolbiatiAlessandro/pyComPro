import unittest
import l453b


class testSolution(unittest.TestCase):
    
    def setUp( self ):
        self.s = l453b.Solution()

    def test_solution( self ):
        nums1 = [4,1,2] 
        nums2 = [1,3,4,2]
        Output= [-1,3,-1]
        got = self.s.nextGreaterElement(nums1, nums2)
        self.assertListEqual(got, Output)
        
        nums1 = [2,4] 
        nums2 = [1,2,3,4]
        Output= [3,-1]
        got = self.s.nextGreaterElement(nums1, nums2)
        self.assertListEqual(got, Output)

        nums1 = [2,4] 
        nums2 = [1,2,3,4]
        Output= [3,-1]
        got = self.s.nextGreaterElement(nums1, nums2)
        self.assertListEqual(got, Output)
        

if __name__ == "__main__":
    unittest.main()

