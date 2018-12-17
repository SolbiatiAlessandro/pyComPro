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


def hack_1(b):
    count = len(b) * 2
    bSeq = b


    aSeq = [0] * count

    for i in range(len(bSeq)):
        if i == 0:
            aSeq[0] = 0
            aSeq[-1] = bSeq[i]
        else:
            '''
            for j in range(bSeq[i] + 1):
                firstHalf = j
                secHalf = bSeq[i] - j
                #print("firstHalf", firstHalf)
                #print("secHalf", secHalf)
                if aSeq[i - 1] <= firstHalf and aSeq[-i] >= secHalf:
                    #print("good")
                    aSeq[i] = firstHalf
                    aSeq[-i-1] = secHalf
                    break
                    '''
            if bSeq[i] <= aSeq[-i]:
                aSeq[i] = aSeq[i-1]
                aSeq[-i-1] = bSeq[i] - aSeq[i-1]
            else:
                if bSeq[i] - aSeq[-i] < aSeq[i-1]:
                    if bSeq[i] - aSeq[-i] < 0:
                        aSeq[i] = bSeq[i] - aSeq[-i]
                        aSeq[-i-1] = aSeq[-i]
                    else:
                        aSeq[i] = aSeq[i-1]
                        aSeq[-i-1] = bSeq[i] - aSeq[i-1]
                else:
                    aSeq[i] = bSeq[i] - aSeq[-i]
                    aSeq[-i-1] = aSeq[-i]

    return aSeq


class test_class(unittest.TestCase):
    def test_basic(self):
        s = hack_1([5,6])
        print s
        self.assertTrue(valid([5,6],s))
        s = hack_1([2,1,2])
        print s
        self.assertTrue(valid([2,1,2],s))
        b = [9, 9, 10, 9, 10, 11]
        s = hack_1(b)
        print s
        self.assertTrue(valid(b,s))
        print "basicOK"

    #@unittest.skip("skip if you can not precompute the answer")
    def test_regression(self):
        from random import random as rnd
        solve = hack_1
        from time import time
        SIZE = 1000 # size of the regression (iterations)
        t1 = time()
        for i in xrange(SIZE):
            # int(rnd() * (upper_bound - lower_bound) + lower_bound) for the parameter
            sequence = sorted([int(rnd() * (1000 - 0)) + 0 for _ in xrange(2*(i + 2))])
            #print sequence
            b = []
            for i in xrange(len(sequence)/2):
                num  = sequence[i]
                b.append(num + sequence[-(i + 1)])
            #print b
            got = solve(b)
            #print got
            self.assertTrue(valid(b, got))
        t2 = time()
        print "regressionOK : "+str(t2 - t1)


if __name__ == "__main__":
    unittest.main()
