import unittest
import A

def hack1(a):
    n = len(a)
    a=[0]+a
    ans = 0
    for i in xrange(1, n+1):
        ans+=a[i]*(i-1)*2
    summ = 0
    minim = 1e9
    for i in xrange(1,n+1):
        summ = 0
        for j in xrange(1,n+1):
            summ+=(abs(i-j)+(i-1))*2*a[j]
        minim = min(minim, summ)
    ans+=minim
    return ans

class test_class(unittest.TestCase):
    def test_basic(self):
        s = A.solve([0,2,1])
        self.assertEqual(s, 16)
        s = A.solve([1,1])
        self.assertEqual(s, 4)
        print "basicOK"

    def test_basic_hack(self):
        s = hack1([0,2,1])
        self.assertEqual(s, 16)
        s = hack1([1,1])
        self.assertEqual(s, 4)
        print "basicOK"

    #@unittest.skip("")
    def test_regression(self):
        from random import random as rnd
        from A import solve
        from time import time
        SIZE = 1000 # size of the regression (iterations)
        t1 = time()
        for _ in xrange(SIZE):
            # int(rnd() * (upper_bound - lower_bound) + lower_bound)
            array = [(int(rnd() * (100 - 0)) + 0) for _ in xrange(int(rnd() * (100 - 1) + 1))]
            true = A.solve(array)
            try:
                self.assertEqual(true, hack1(array))
            except:
                print array
                exit()
        t2 = time()
        print "regressionOK : "+str(t2 - t1)


if __name__ == "__main__":
    unittest.main()
