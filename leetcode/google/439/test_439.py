import unittest
import l439


class testSolution(unittest.TestCase):
    
    def setUp( self ):
        self.s = l439.Solution()

    def test_solution( self ):
        nums = [1,3,1]
        k = 1
        got = self.s.smallestDistancePair(nums, k)
        self.assertEqual(got, 0)

        nums = [1,2,3,4,5]
        expected = [1,1,1,1,2,2,2,3,3,4]
        for x in xrange(1, 11):
            got = self.s.smallestDistancePair(nums, x)
            self.assertEqual(got, expected[x-1])

        nums = [0, 0]
        k = 1
        got = self.s.smallestDistancePair(nums, k)
        self.assertEqual(got, 0)

    def test_custom(self):
        nums = [9,10,7,10,6,1,5,4,9,8]
        got = self.s.smallestDistancePair(nums, 18)
        self.assertEqual(got, 2)
            

if __name__ == "__main__":
    unittest.main()

