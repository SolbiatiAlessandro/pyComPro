import unittest
import l461


class testSolution(unittest.TestCase):
    
    def setUp( self ):
        self.s = l461.Solution()

    def test_solution( self ):
        nums = [0,1,0,2,3]
        self.s.moveZeroes(nums)
        self.assertEqual(nums, [1,2,3,0,0])

        nums = [0]
        self.s.moveZeroes(nums)
        self.assertEqual(nums, [0])

        nums = [0,1]
        self.s.moveZeroes(nums)
        self.assertEqual(nums, [1,0])

        nums = []
        self.s.moveZeroes(nums)
        self.assertEqual(nums, [])

        nums = [0,3,4,5,6]
        self.s.moveZeroes(nums)
        self.assertEqual(nums, [3,4,5,6,0])

        nums = [3,4,5,6]
        self.s.moveZeroes(nums)
        self.assertEqual(nums, [3,4,5,6])
        

if __name__ == "__main__":
    unittest.main()

