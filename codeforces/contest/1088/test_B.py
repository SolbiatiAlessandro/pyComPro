import unittest
import B2

class test_class(unittest.TestCase):
    def test_basic(self):
        s = B2.solve(3, 5, [1, 2, 3])
        self.assertEqual(s, [1, 1, 1, 0, 0])

        s = B2.solve(4, 2, [10, 3, 5, 3])
        self.assertEqual(s, [3, 2])

        s = B2.solve(5, 100, [10, 3, 3, 3, 3, 3, 5, 3])
        #self.assertEqual(s, [3, 2])
        print "basicOK"

    @unittest.skip("skip if you can not precompute the answer")
    def test_regression(self):
        from random import random as rnd
        from B2 import solve
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
