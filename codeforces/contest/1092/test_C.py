import unittest
import C

class test_class(unittest.TestCase):
    def test_basic(self):
        s = C.solve([['a', 0], ['aa', 1], ['aa', 2], ['a', 3]])
        self.assertEqual(s, "PPSS")
        print "basicOK"

    #@unittest.skip("skip if you can not precompute the answer")
    def test_regression(self):
        from random import random as rnd
        from C import solve
        from time import time
        SIZE = 100000 # size of the regression (iterations)
        t1 = time()
        for _ in xrange(SIZE):
            # int(rnd() * (upper_bound - lower_bound) + lower_bound) for the parameter
            n = int(rnd() * (10 - 2)) + 2
            string = ""
            for i in xrange(n):
                string += (chr(ord('a') + int(rnd() * 23)))
            #print string
            subs = []
            for i in xrange(1, n):
                subs.append([string[:i], i - 1])
            for j in xrange(1, n):
                subs.append([string[-j:], j+i-1])
            print string
            print subs
            #print len(subs)
            #print n
            got = solve(subs)
            print got
            N = len(subs)
            self.assertTrue(got[:N/2] ==  'P'*(N/2) or got[:N/2] ==  'S'*(N/2)) 
            self.assertTrue(got[N/2:] ==  'P'*(N/2) or got[N/2:] ==  'S'*(N/2)) 
            
        t2 = time()
        print "regressionOK : "+str(t2 - t1)


if __name__ == "__main__":
    unittest.main()
