import unittest
import B

def valid(n, k, res):
    return (res / k) * (res % k) == n

class test_class(unittest.TestCase):
    def test_basic(self):
        s = B.solve(6,3)
        self.assertEqual(s, 11)
        self.assertTrue(valid(6,3,int(s)))
        s = B.solve(1,2)
        self.assertEqual(s, 3)
        self.assertTrue(valid(1,2,int(s)))
        s = B.solve(4,6)
        self.assertTrue(valid(4,6,int(s)))
        self.assertEqual(s, 10)
        print "basicOK"

    #@unittest.skip("skip if you can not precompute the answer")
    def test_regression(self):
        from random import random as rnd
        from B import solve
        from time import time
        SIZE = 1000 # size of the regression (iterations)
        t1 = time()
        for _ in xrange(SIZE):
            # int(rnd() * (upper_bound - lower_bound) + lower_bound) for the parameter
            n = (int(rnd() * (100 - 0)) + 0)
            k = (int(rnd() * (10 - 2)) + 2)
            got = solve(
                    n,k
                    )
            try:
                self.assertTrue(valid(n,k,got))
            except:
                print n,k,got
                exit("")
        t2 = time()
        print "regressionOK : "+str(t2 - t1)


if __name__ == "__main__":
    unittest.main()
