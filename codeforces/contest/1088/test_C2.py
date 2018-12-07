import unittest
import C2

def is_increasing(a):
    for i, num in enumerate(a[:-1]):
        if a[i + 1] <= num: return False
    return True

class test_class(unittest.TestCase):
    def test_basic(self):
        s = C2.solve([1,2,3])
        self.assertTrue(is_increasing(s))
        s = C2.solve([7,6,3])
        self.assertTrue(is_increasing(s))
        print "basicOK"

    #@unittest.skip("skip if you can not precompute the answer")
    def test_regression(self):
        from random import random as rnd
        from C2 import solve
        from time import time
        SIZE = 1000 # size of the regression (iterations)
        t1 = time()
        for _ in xrange(SIZE):
            # int(rnd() * (upper_bound - lower_bound) + lower_bound) for the parameter
            got = solve(
                    [(int(rnd() * (100000 - 0)) + 0) for _ in xrange (int(rnd() * (2000 - 1)) + 1)]
                    )
            self.assertTrue(is_increasing(got))
        t2 = time()
        print "regressionOK : "+str(t2 - t1)


if __name__ == "__main__":
    unittest.main()
