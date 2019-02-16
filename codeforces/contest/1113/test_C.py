import unittest
import C

from C import solve

class test_class(unittest.TestCase):
    def test_basic(self):
        s = solve([3,2,2,3,7,6])
        self.assertEqual(s, 3)
        s = solve([1,2,3,5,6,7])
        self.assertEqual(s, 0)
        s = solve([1,2,3,5,6,3])
        self.assertEqual(s, 1)
        s = solve([2,3,10,11])
        self.assertEqual(s, 1)
        s = solve([2,5,3,10,5,11])
        self.assertEqual(s, 1)
        s = solve([6,1,22,17])
        self.assertEqual(s, 1)
        s = solve([6,1,17,22])
        self.assertEqual(s, 1)
        print("complicated")
        s = solve([6,1,2,3,10,11,17,22])
        self.assertEqual(s, 2)
        print("complicated")
        s = solve([6,1,2,12312,3,10,11,17,22,12312])
        self.assertEqual(s, 1)
        print("complicated")
        s = solve([6,1,2,5,3,10,11,17,22,5])
        print('toomany')
        s = solve([1,1,1,1,1])
        n = 100
        print n
        print(solve([1 for _ in xrange(n)], verbose=False))
        n = 1000
        print n
        print(solve([1 for _ in xrange(n)], verbose=False))
        n = 10000
        print n
        print(solve([1 for _ in xrange(n)], verbose=False))
        print "basicOK"

    @unittest.skip("skip if you can not precompute the answer")
    def test_regression(self):
        from random import random as rnd
        from C import solve
        from time import time
        SIZE = 1000 # size of the regression (iterations)
        t1 = time()
        for _ in xrange(SIZE):
            # int(rnd() * (upper_bound - lower_bound) + lower_bound) for the parameter
            arr = [(int(rnd() * (10 - 0)) + 0) for i in xrange(10000)]
            #print arr
            got = solve(arr)
        t2 = time()
        print "regressionOK : "+str(t2 - t1)


if __name__ == "__main__":
    unittest.main()
