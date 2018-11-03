import unittest
import l439c
import custom_input


class testSolution(unittest.TestCase):
    
    def setUp( self ):
        self.s = l439c.Solution()

    #@unittest.skip("Wait")
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

    #@unittest.skip("Wait")
    def test_custom(self):
        nums = [9,10,7,10,6,1,5,4,9,8]
        nums.sort()
        nums.append(1e9)
        start, end = l439c.compute_range(nums, 0)
        for distance in xrange(1,10):
            prev = end
            start, end = l439c.compute_range(nums, distance)
            try:
                self.assertEqual(start, prev)
            except Exception as e:
                print e
                print distance, start, end
        nums = [9,10,7,10,6,1,5,4,9,8]
        got = self.s.smallestDistancePair(nums, 18)
        self.assertEqual(got, 2)


    #@unittest.skip("Wait")
    def test_range(self):
        nums = [1,3,4,5,5,9]
        nums.append(1e9)
        a, b = l439c.compute_range(nums, 4)
        self.assertEqual((a,b),(8,12))
        a, b = l439c.compute_range(nums, 2)
        self.assertEqual((a,b),(4,7))
        a, b = l439c.compute_range(nums, 2.5)
        self.assertEqual((a,b),(7,7))
        a, b = l439c.compute_range(nums, 1)
        self.assertEqual((a,b),(1,4))
        a, b = l439c.compute_range(nums, 0)
        self.assertEqual((a,b),(0,1))
        a, b = l439c.compute_range(nums, 5)
        self.assertEqual((a,b),(12,13))
        a, b = l439c.compute_range(nums, 3)
        self.assertEqual((a,b),(7,8))

        print "basic range ok"

        #import pdb;pdb.set_trace()
        nums = [1,3,4,5,5,9]
        got = self.s.smallestDistancePair(nums, 9)
        self.assertEqual(got, 4)

        distances = [0,1,1,1,2,2,2,3,4,4,4,4,5]
        for i, distance in enumerate(distances):
            try:
                got = self.s.smallestDistancePair(nums, i+1)
                self.assertEqual(got, distance)
            except Exception as e:
                print e, i+1, distance

        print "range basic is okk"

    #@unittest.skip("wait")
    def test_profile(self):
        nums = [0] * 4000
        from time import time
        t1 = time()
        got = self.s.smallestDistancePair(nums, 99)
        t2 = time()
        self.assertEqual(got, 0)
        print t2 - t1

    #@unittest.skip("wait")
    def test_custom_tle(self):
        nums = custom_input.nums
        from time import time
        t1 = time()
        got = self.s.smallestDistancePair(nums, custom_input.k)
        t2 = time()
        #self.assertEqual(got, 0)
        print "len(200), k=10000"
        print t2 - t1

    #@unittest.skip("wait")
    def test_range_continguos(self):
        nums = [0,0,0,1,1,1,2,2,2]
        nums.append(1e9)
        got = l439c.compute_range(nums, 0)
        self.assertEqual(got, (0,9))
        got = l439c.compute_range(nums, 1)
        self.assertEqual(got, (9,27))
        got = l439c.compute_range(nums, 2)
        self.assertEqual(got, (27,36))

        print "rangok"


if __name__ == "__main__":
    unittest.main()

