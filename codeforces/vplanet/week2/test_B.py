import unittest
import B

class test_class(unittest.TestCase):
    def test_basic(self):
        s = B.solve([1,2,3],1,3)
        self.assertEqual(s, 3)
        s = B.solve([1,2,3,4,1],1,3)
        self.assertEqual(s, 4)
        s = B.solve([5,2,3,4,5],1,3)
        self.assertEqual(s, 2)
        s = B.solve([1,3,3,1,1,3,3,1],1,3)
        self.assertEqual(s, 4)
        print "basicOK"

    @unittest.skip("skip if you can not precompute the answer")
    def test_regression(self):
        from random import random as rnd
        from B import solve
        from time import time
        SIZE = 1000 # size of the regression (iterations)
        t1 = time()
        for _ in xrange(SIZE):
            # int(rnd() * (upper_bound - lower_bound) + lower_bound) for the parameter
            got = solve(
                    (int(rnd() * (1000 - 0)) + 0),
                    (int(rnd() * (1000 - 1)) + 1)
                    )
            self.assertEqual(got, -1)
        t2 = time()
        print "regressionOK : "+str(t2 - t1)


if __name__ == "__main__":
    unittest.main()
