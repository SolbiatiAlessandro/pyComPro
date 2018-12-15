import unittest
import C

def valid(b, a):
    #import pdb;pdb.set_trace()
    for i, num in enumerate(a[:-1]):
        if num > a[i + 1]: return False
    for i, num in enumerate(b):
        if a[i] + a[len(a)-1-i] != b[i]:
            return False
    return True

class test_class(unittest.TestCase):
    def test_basic(self):
        s = C.solve([5,6])
        print s
        self.assertTrue(valid([5,6],s))
        s = C.solve([2,1,2])
        print s
        self.assertTrue(valid([2,1,2],s))
        b = [9, 9, 10, 9, 10, 11]
        s = C.solve(b)
        print s
        self.assertTrue(valid(b,s))
        print "basicOK"

    #@unittest.skip("skip if you can not precompute the answer")
    def test_regression(self):
        from random import random as rnd
        from C import solve
        from time import time
        SIZE = 100 # size of the regression (iterations)
        t1 = time()
        for i in xrange(SIZE):
            # int(rnd() * (upper_bound - lower_bound) + lower_bound) for the parameter
            sequence = sorted([int(rnd() * (10 - 0)) + 0 for _ in xrange(2*(i + 2))])
            print sequence
            b = []
            for i in xrange(len(sequence)/2):
                num  = sequence[i]
                b.append(num + sequence[-(i + 1)])
            print b
            got = solve(b)
            print got
            self.assertTrue(valid(b, got))
        t2 = time()
        print "regressionOK : "+str(t2 - t1)


if __name__ == "__main__":
    unittest.main()
