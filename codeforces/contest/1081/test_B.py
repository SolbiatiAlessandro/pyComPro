import unittest
import B1

class test_class(unittest.TestCase):
    def test_basic(self):
        s = B1.solve([0,0,0])
        self.assertEqual(s, [1,1,1])
        s = B1.solve([3,3,2,2,2])
        self.assertEqual(s, [1,1,2,2,2])
        s = B1.solve([0,1,2,3])
        self.assertEqual(s, -1)
        s = B1.solve([0])
        self.assertEqual(s, [1])
        s = B1.solve([5,5,5,5,5,5])
        self.assertNotEqual(s, -1)
        print "basicOK"

    @unittest.skip("skip if you can not precompute the answer")
    def test_regression(self):
        from random import random as rnd
        from B1 import solve
        from time import time
        SIZE = 1000 # size of the regression (iterations)
        t1 = time()
        for _ in xrange(SIZE):
            x = 10
            # int(rnd() * (upper_bound - lower_bound) + lower_bound) for the parameter
            nums = [(int(rnd() * (x - 0)) + 0) for _ in xrange(x)]
            got = solve(nums)
            from collections import Counter
            self.assertEqual(got, -1)
        t2 = time()
        print "regressionOK : "+str(t2 - t1)


if __name__ == "__main__":
    unittest.main()
