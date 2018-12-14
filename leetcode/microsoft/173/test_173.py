import unittest
import l173b


class testSolution(unittest.TestCase):
    
    def setUp( self ):
        self.s = l173b.Solution()

    def test_solution( self ):
        nums = [2, 7, 11, 15]
        target = 9
        got = self.s.twoSum(nums, target)
        self.assertEqual(got, (0, 1))
        
        nums = [2,7,11,15]
        target = 26
        got = self.s.twoSum(nums, target)
        self.assertEqual(got, (2, 3))

        nums = [20,2,9,19,7,11,15]
        target = 9
        got = self.s.twoSum(nums, target)
        self.assertEqual(got, (1, 4))

        nums = [2,7]
        target = 9
        got = self.s.twoSum(nums, target)
        self.assertEqual(got, (0, 1))

        nums = [7,2]
        target = 9
        got = self.s.twoSum(nums, target)
        self.assertEqual(got, (0, 1))

        nums = [0,0,0,0,0,7,2,0,0,0]
        target = 9
        got = self.s.twoSum(nums, target)
        self.assertEqual(got, (5, 6))

        from random import random as rnd
        from time import time as t
        for _ in xrange(3):
            l = 50
            nums = [x for x in xrange(l)]
            for i in xrange(l):
                for j in xrange(l):
                    if i != j:
                        target = nums[i]+nums[j]
                        t1 = t()
                        got = self.s.twoSum(nums, target)
                        print(t()-t1)
                        try:
                            self.assertEqual(nums[got[0]]+nums[got[1]], nums[i]+nums[j])
                        except:
                            print nums
                            print nums[i], nums[j]
                            print i, j
                            print got
                            exit('random test failed')



if __name__ == "__main__":
    unittest.main()

