import unittest
import l457


class testSolution(unittest.TestCase):
    
    def setUp( self ):
        self.s = l457.Solution()

    def test_solution( self ):

        got = self.s.firstMissingPositive([1,2,0])
        self.assertEqual(got, 3)
        got = self.s.firstMissingPositive([3,4,-1,1])
        self.assertEqual(got, 2)
        got = self.s.firstMissingPositive([7,8,9,11,12])
        self.assertEqual(got, 1)
        got = self.s.firstMissingPositive([7,5,4,3,2,1])
        self.assertEqual(got, 6)
        got = self.s.firstMissingPositive([7,5,4,3,2,1])
        self.assertEqual(got, 6)
        got = self.s.firstMissingPositive([0,-1,-2])
        self.assertEqual(got, 1)
        got = self.s.firstMissingPositive([1,-1,-2])
        self.assertEqual(got, 2)
        got = self.s.firstMissingPositive([1,1,2])
        self.assertEqual(got, 3)



if __name__ == "__main__":
    unittest.main()
