import unittest
import C

class test_class(unittest.TestCase):
    def test_basic(self):
        s = C.solve(16)
        self.assertEqual(s, [1, 10, 28, 64, 136])
        s = C.solve(6)
        self.assertEqual(s, [1, 5, 9, 21])
        s = C.solve(2)
        self.assertEqual(s, [1, 3])
        s = C.solve(3)
        self.assertEqual(s, [1, 6])
        print "basicOK"

    #@unittest.skip("skip if you can not precompute the answer")
    def test_regression(self):
        from random import random as rnd
        from C import solve
        from time import time
        SIZE = 1000 # size of the regression (iterations)
        t1 = time()
        """for _ in xrange(SIZE):
            # int(rnd() * (upper_bound - lower_bound) + lower_bound) for the parameter
            got = solve(
                    (int(rnd() * (1000 - 0)) + 0),
                    (int(rnd() * (1000 - 1)) + 1)
                    )
            self.assertEqual(got, -1)"""
        s = C.solve(pow(10, 9) - 2)
        t2 = time()
        print "regressionOK : "+str(t2 - t1)


if __name__ == "__main__":
    unittest.main()
