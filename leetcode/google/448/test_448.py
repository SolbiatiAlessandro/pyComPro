import unittest
import l448


class testSolution(unittest.TestCase):
    
    def setUp( self ):
        self.s = l448.Solution()

    #@unittest.skip("")
    def test_solution_A( self ):
        nums = [-4,-2,2,4]
        a = 1
        b = 3
        c = 5
        output = [3,9,15,33]
        got = self.s.sortTransformedArray(nums, a, b, c)
        self.assertEqual(got, output)

    def test_solution_B( self ):
        nums = [-4,-2,2,4]
        a = -1
        b = 3
        c = 5
        output = [-23,-5,1,7]
        #import pdb;pdb.set_trace()
        got = self.s.sortTransformedArray(nums, a, b, c) 
        self.assertEqual(got, output)

        nums = [-4,-2]
        a = -1
        b = 3
        c = 5
        output = [-23,-5]
        got = self.s.sortTransformedArray(nums, a, b, c) 
        self.assertEqual(got, output)

        nums = [2,4]
        a = -1
        b = 3
        c = 5
        output = [1,7]
        got = self.s.sortTransformedArray(nums, a, b, c) 
        self.assertEqual(got, output)

        nums = [-2,4]
        a = -1
        b = 3
        c = 5
        output = [-5,1]
        got = self.s.sortTransformedArray(nums, a, b, c) 
        self.assertEqual(got, output)

        nums = [-4,-2,2,4]
        a = 0
        b = 3
        c = 5
        def transform(num):
            return a*num*num + b*num + c
        output = sorted([transform(num) for num in nums])
        #import pdb;pdb.set_trace()
        got = self.s.sortTransformedArray(nums, a, b, c) 
        self.assertEqual(got, output)

        nums = [-4,-2,2,4]
        a = 0
        b = -3
        c = 5
        def transform(num):
            return a*num*num + b*num + c
        output = sorted([transform(num) for num in nums])
        #import pdb;pdb.set_trace()
        got = self.s.sortTransformedArray(nums, a, b, c) 
        self.assertEqual(got, output)

        nums = [-4,-2,2,4]
        a = 0
        b = 0
        c = 5
        def transform(num):
            return a*num*num + b*num + c
        output = sorted([transform(num) for num in nums])
        #import pdb;pdb.set_trace()
        got = self.s.sortTransformedArray(nums, a, b, c) 
        self.assertEqual(got, output)

        nums = [-4,-1,0]
        a = 4
        b = 7
        c = 8
        def transform(num):
            return a*num*num + b*num + c
        output = sorted([transform(num) for num in nums])
        #import pdb;pdb.set_trace()
        got = self.s.sortTransformedArray(nums, a, b, c) 
        self.assertEqual(got, output)


    #@unittest.skip("")
    def test_random(self):
        from random import random
        for _ in xrange(10000):
            l = int(random()*25)
            a,b,c = int(random()*20 - 10),int(random()*20 - 10),int(random()*20 - 10)
            nums = []
            for __ in xrange(l):
                nums.append(int(random()*2000 - 1000))
            nums.sort()
            def transform(num):
                return a*num*num + b*num + c
            output = sorted([transform(num) for num in nums])
            got = self.s.sortTransformedArray(nums, a, b, c) 
            try:
                self.assertEqual(got, output)
            except Exception as e:
                print e
                print nums
                print output, got
                print a,b,c
                exit("not ready")


if __name__ == "__main__":
    unittest.main()
