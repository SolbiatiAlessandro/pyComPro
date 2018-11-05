import unittest
import l440


class testSolution(unittest.TestCase):
    
    def setUp( self ):
        self.api = l440.RangeModule()

    def test_bs(self):
        bs = l440.binary_search  
        nums = [10,14,16,20]
        got = bs(nums, 5)
        self.assertEqual(got, -1)
        got = bs(nums, 10)
        self.assertEqual(got, 0)
        got = bs(nums, 11)
        self.assertEqual(got, 0)
        got = bs(nums, 14)
        self.assertEqual(got, 1)
        got = bs(nums, 15)
        self.assertEqual(got, 1)
        got = bs(nums, 16)
        self.assertEqual(got, 2)
        got = bs(nums, 17)
        self.assertEqual(got, 2)
        got = bs(nums, 18)
        self.assertEqual(got, 2)
        got = bs(nums, 20)
        self.assertEqual(got, 3)
        got = bs(nums, 21)
        self.assertEqual(got, 3)

    #@unittest.skip("")
    def test_solution( self ):
        self.api.addRange(10, 20)
        self.api.removeRange(14, 16)
        self.assertListEqual(self.api.nums, [10,14,16,20])
        got = self.api.queryRange(10, 14)
        self.assertTrue(got)
        got = self.api.queryRange(10, 15)
        self.assertFalse(got)
        got = self.api.queryRange(16, 17)
        self.assertTrue(got)
        print "okk"


if __name__ == "__main__":
    unittest.main()
