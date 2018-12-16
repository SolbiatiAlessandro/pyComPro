import unittest
import C

class test_class(unittest.TestCase):
    def test_basic(self):
        s = C.solve(3,3,0)
        self.assertEqual(s, 3)
        s = C.solve(3,2,1)
        self.assertEqual(s, 4)
        s = C.solve(1,1,0)
        self.assertEqual(s, 1)
        s = C.solve(1,10,0)
        self.assertEqual(s, 10)
        s = C.solve(5,2,0)
        self.assertEqual(s, 2)
        print "bbasicOK"

    @unittest.skip("skip if you can not precompute the answer")
    def test_regression(self):
        from random import random as rnd
        from C import solve
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
