import unittest
import l439_heap
import custom_input
import custom_input_long


class testSolution(unittest.TestCase):
    
    def setUp( self ):
        self.s = l439_heap.Solution()

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

    def test_profile(self):
        nums = [0] * 4000
        from time import time
        t1 = time()
        got = self.s.smallestDistancePair(nums, 99)
        t2 = time()
        self.assertEqual(got, 0)
        print t2 - t1

    def test_custom_tle(self):
        nums = custom_input.nums
        from time import time
        t1 = time()
        got = self.s.smallestDistancePair(nums, custom_input.k)
        t2 = time()
        #self.assertEqual(got, 0)
        print "len(200), k=10000"
        print t2 - t1

    def test_custom_tle(self):
        nums = custom_input_long.nums
        from time import time
        t1 = time()
        got = self.s.smallestDistancePair(nums, custom_input_long.k)
        t2 = time()
        #self.assertEqual(got, 0)
        print "len(nums) = 10000"
        print t2 - t1


if __name__ == "__main__":
    unittest.main()

