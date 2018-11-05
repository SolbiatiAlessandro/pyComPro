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

        # remove from left
        self.api.removeRange(15, 18)
        self.assertListEqual(self.api.nums, [10,14,18,20])
        # remove from right
        self.api.removeRange(12, 16)
        self.assertListEqual(self.api.nums, [10,12,18,20])
        # remove from both outside
        self.api.removeRange(15, 22)
        self.assertListEqual(self.api.nums, [10,12])
        # add to outside
        self.api.addRange(20, 30)
        self.assertListEqual(self.api.nums, [10,12,20,30])
        # add from inside
        self.api.addRange(24, 27)
        self.assertListEqual(self.api.nums, [10,12,20,30])
        # remove from inside
        self.api.removeRange(24, 27)
        self.assertListEqual(self.api.nums, [10,12,20,24,27,30])
        # remove from left inside and raddRight inside
        self.api.removeRange(23, 28)
        self.assertListEqual(self.api.nums, [10,12,20,23,28,30])
        self.api.removeRange(12, 21)
        self.assertListEqual(self.api.nums, [10,12,21,23,28,30])
        self.api.removeRange(11, 29)
        self.assertListEqual(self.api.nums, [10,11,29,30])
        # remove all
        self.api.removeRange(0, 1000000000)
        self.assertListEqual(self.api.nums, [])
        self.api.addRange(20, 100)
        self.assertListEqual(self.api.nums, [20, 100])
        # add from left
        self.api.addRange(15, 50)
        self.assertListEqual(self.api.nums, [15, 100])
        # add from right
        self.api.addRange(85, 150)
        self.assertListEqual(self.api.nums, [15, 150])
        # add from inside
        self.api.addRange(85, 150)
        self.assertListEqual(self.api.nums, [15, 150])
        self.api.addRange(85, 120)
        self.assertListEqual(self.api.nums, [15, 150])
        # add from outside
        self.api.addRange(5, 250)
        self.assertListEqual(self.api.nums, [5, 250])
        self.api.addRange(555, 1250)
        self.assertListEqual(self.api.nums, [5, 250, 555, 1250])
        # add from in between
        self.api.addRange(155, 1050)
        self.assertListEqual(self.api.nums, [5, 1250])
        self.api.removeRange(85, 120)
        self.assertListEqual(self.api.nums, [5, 85, 120, 1250])

        #query test left
        self.assertFalse(self.api.queryRange(3, 9))
        self.assertFalse(self.api.queryRange(90, 129))
        #query test right
        self.assertFalse(self.api.queryRange(80, 90))
        self.assertFalse(self.api.queryRange(1250, 1299))
        #query test all
        self.assertFalse(self.api.queryRange(1, 11190))

        #query test true
        self.assertTrue(self.api.queryRange(10, 20))
        self.assertTrue(self.api.queryRange(5, 20))
        self.assertTrue(self.api.queryRange(5, 85))
        self.assertFalse(self.api.queryRange(5, 86))

        
        print "okk"


if __name__ == "__main__":
    unittest.main()
